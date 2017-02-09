/**
 * Created by margin on 2017/1/18.
 */

// 添加扫描任务页面停止标志
var kill_flag;
// 查看扫描日志界面停止标志
var readlogInterval;
var taskids = [];
$(function() {
    var $table = $('#overview');
    $table.bootstrapTable('destroy');
    $table.bootstrapTable({
        url: "/SQLMapUI/alltasks/",
        method:"post",
        dataType: "json",
        pagination: true, //分页
        contentType: "application/x-www-form-urlencoded",
        singleSelect: false,
        search: true, //显示搜索框
        //sidePagination: "client", //服务端处理分页
        striped: true,  //表格显示条纹
        pagination: true, //启动分页
        pageSize: 10,  //每页显示的记录数
        pageNumber:1, //当前第几页
        pageList: [10, 20, 30, 40],  //记录数可选列表
        showRefresh:true,
        toolbar: '#toolbar',
        columns: [
            {
                title: '扫描ID',
                field: 'id',
                align: 'center',
                valign: 'middle'
            },
            {
                  title: '扫描状态',
                  field: 'status',
                  align: 'center',
                  valign: 'middle'
            },
            {
                  title: '扫描结果',
                  field: 'result',
                  align: 'center'
            },
            {
                  title: '开始时间',
                  field: 'start_time',
                  align: 'center'
            },
            {
                  title: '实时时间',
                  field: 'end_time',
                  align: 'center'
            },
            {
                  title: '操作',
                  align: 'center',
                  formatter:function(value,row,index){
                      var read = '<button type="button" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#task_log" onclick="read(\''+ row.id + '\' , \'' +row.status + '\')">查看</button> ';
                      var stop = '<button type="button" class="btn btn-warning btn-xs" onclick="stop(\''+ row.id + '\')">停止</button> ';
                      var del = '<button type="button" class="btn btn-danger btn-xs" onclick="del_task(\''+ row.id + '\')">删除</button> ';
                      return read+stop+del;
                  }
            }
        ],
        onLoadSuccess:function(data){
            //alert(JSON.stringify(data));
        },
        onLoadError:function(data){
            //alert(data);
        }
    });
    $("#kill").click(function(){
        // 清除前台的轮训查询
        clearInterval(readlogInterval);
        clearInterval(kill_flag);
        // stop掉后台的扫描任务
        stop(taskids);
        $("#bash").removeClass('disabled');
        $("#start").removeClass('disabled');
    });
    $("#start").click(function(){
        // sqlmap 参数对象
        var data = {};
        var url = $("#url").val()
        // 分解sqlmap命令
        var url_ = url.split(" ");
        url_.splice(0,1);
        var key_ = "";
        var value_ = "";
        for (var i = 0; i < url_.length / 2; i++) {
            key_ = url_[i * 2].replace(/-/g, "");
            if (key_ == "u"){
                key_ = "url";
            }
            value_ = url_[i * 2 + 1];
            data[key_] = value_;
        }
        alert(JSON.stringify(data));
        start(data);
        $("#bash").addClass('disabled');
        $("#start").addClass('disabled');
    });
    $("#bash").click(function(){
        var data = {"url":$("#url").val(),"bash":"1"};
        start(data);
        $("#bash").addClass('disabled');
        $("#start").addClass('disabled');
    });
    $('#task_log').on('hidden.bs.modal', function (e) {
        clearInterval(readlogInterval);
    });
    $('#flush').click(function(){
        $.ajax({
            type: 'POST',
            url: "/SQLMapUI/web_flush/",
            data: JSON.stringify({}),
            success: function(data, status){
                $('#overview').bootstrapTable('refresh');
            },
            dataType: "json"
        });
    });
    var logwating;
    // 端口扫描按钮事件
    $('#port_scan_start').click(function(){
        $("#port_scan_start").addClass('disabled');
        var count = 0;
        logwating = setInterval(function () {
            count+=1;
            $("#port_scan_log").html("NMap扫描进度不能实时显示，所以请稍后。当前用时[" + count + "]秒。");
        }, 1000);
        var data = {"host":"","port":"","arguments":""}
        var commond = $("#port_scan_commond").val();
        //commond = "nmap -p1-65535 -T4 -A -v -Pn 127.0.0.1";
        var commonds = commond.split(" ");
        var reg_port = /^\-p\d{0,5}\-\d{0,5}/;
        var tmp;
        $.each(commonds, function(index, value){
            tmp = value.match(reg_port);
            if (tmp){
                data.port = tmp[0].substring(2,tmp[0].length);
            }
        });
        data.host = commonds[commonds.length-1];
        data.arguments = commond.replace(data.host,"").replace("-p"+data.port,"").replace("nmap","");
        //alert(JSON.stringify(data));
        $.ajax({
            type: 'POST',
            url: "/SQLMapUI/port_scaner/",
            data: JSON.stringify(data),
            success: function(data, status){
                clearInterval(logwating);
                $("#port_scan_start").removeClass('disabled');
                read_file(data.data);
            },
            error: function(data,status){
                clearInterval(logwating);
                $("#port_scan_start").removeClass('disabled');
                $("#port_scan_log").html("扫描失败。用时[" + count + "]秒。");
            },
            dataType: "json"
        });

    });
});
function start(data){
    $.ajax({
        type: 'POST',
        url: "/SQLMapUI/bash_task/",
        data: JSON.stringify(data),
        success: function(data, status){
            // 获取返回的taskid
            taskids = data["taskid"]
            if(data["success"] == true){
                kill_flag = setInterval(function(){
                    web_log("logging",data);
                },200);
            }
        },
        dataType: "json"
    });
}
function stop(taskid){
    data = {"taskid":taskid};
    if(typeof(taskid) == "string"){
        data = {"taskid":[taskid]};
    }
    $.ajax({
        type: 'POST',
        url: "/SQLMapUI/task_stop/",
        data: JSON.stringify(data),
        success: function(data, status){
            $("#success").alert();
        },
        error: function(data){
            $("#errotext").val(data["msg"]);
            $("#error").alert();
        },
        dataType: "json"
    });
    $('#overview').bootstrapTable('refresh');
}

function del_task(taskid){
    data = {"taskid":taskid};
    if(typeof(taskid) == "string"){
        data = {"taskid":[taskid]};
    }
    $.ajax({
        type: 'POST',
        url: "/SQLMapUI/web_delete/",
        data: JSON.stringify(data),
        success: function(data, status){
            $('#overview').bootstrapTable('refresh');
            alert(data["msg"]);
        },
        error: function(data){
            //$("#errotext").val(data["msg"]);
            alert(JSON.stringify(data));
        },
        dataType: "json"
    });
}

function read(taskid,status){
    if (status == "running") {
        readlogInterval = setInterval(function () {
            web_log("read_logging", {"taskid": taskid});
        }, 200);
    }else {
        web_log("read_logging", {"taskid": taskid});
    }
}
function web_log(logid,data){
    $.ajax({
        type: 'POST',
        url: "/SQLMapUI/web_log/",
        data: JSON.stringify(data),
        success: function(data, status){
            var log = "";
            $.each(data, function(index, value) {
                log = log + value["message"] + "\n";
            });
            $("#" + logid).html(log);
        },
        dataType: "json"
    });
}

function read_file(path){
    var data = {"path":path};
    $.ajax({
        type: 'POST',
        url: "/SQLMapUI/read_file/",
        data: JSON.stringify(data),
        success: function(data, status){
            $("#port_scan_log").html(data.data);
        },
        dataType: "json"
    });
}