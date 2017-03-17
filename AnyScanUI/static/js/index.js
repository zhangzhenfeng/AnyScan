/**
 * Created by margin on 2017/1/18.
 */

// 添加扫描任务页面停止标志
var kill_flag;
// 查看扫描日志界面停止标志
var readlogInterval;
// 端口爆破轮询对象
var attackportlogInterval;
// Sqlmap扫描任务id列表
var taskids = [];
var port_scan_tree;
// 记录当前暴力破解任务的id
var current_port_attack_id = "";
// 记录当前爆破任务的状态
var current_port_attack_status = "pause";
// 查看具体爆破任务的id
var portattackid = ""
// 记录端口暴力破解success次数，连续3次后停止轮询
var port_attack_success_num = 0;
// 读取cms识别日志任务
var cms_scan_log_interval;
// 记录cms识别任务id
var cms_scan_ids;
// 定义百度，Google采集url轮询任务
var poc_url_interval;
// 定义POC执行日志轮询任务
var poc_exec_log_interval;

$(function() {
    var $table = $('#overview');
    $table.bootstrapTable('destroy');
    // 初始化sqlmap任务列表
    $table.bootstrapTable({
        url: "/AnyScanUI/alltasks/",
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
    // 端口爆破任务的table
    //var port_attack_table = $('#port_attack_table');
    //port_attack_table.bootstrapTable('destroy');
    // 初始化端口爆破任务列表
    $('#port_attack_table').bootstrapTable({
        url: "/AnyScanUI/portattack_list/",
        //data:[{'status': '', 'start_time': '', 'end_time': '', 'progress': '', 'type': '', 'id': '3c20ff51-f9ab-11e6-9411-784f435e6bbf'}, {'status': '', 'start_time': '', 'end_time': '', 'progress': '', 'type': '', 'id': '489573e3-f9ab-11e6-8974-784f435e6bbf'}, {'status': '', 'start_time': '', 'end_time': '', 'progress': '', 'type': '', 'id': '8a7bb378-f9aa-11e6-88db-784f435e6bbf'}, {'status': '', 'start_time': '', 'end_time': '', 'progress': '', 'type': '', 'id': 'e98cfd2e-f9ab-11e6-a7d5-784f435e6bbf'}, {'status': '', 'start_time': '', 'end_time': '', 'progress': '', 'type': '', 'id': 'ea2a3475-f9a9-11e6-8b62-784f435e6bbf'}],
        method:"post",
        dataType: "json",
        pagination: true, //分页
        contentType: "application/x-www-form-urlencoded",
        singleSelect: false,
        search: true, //显示搜索框
        striped: true,  //表格显示条纹
        pagination: true, //启动分页
        pageSize: 10,  //每页显示的记录数
        pageNumber:1, //当前第几页
        pageList: [10, 20, 30, 40],  //记录数可选列表
        showRefresh:true,
        //toolbar: '#port_attack_toolbar',
        columns: [
            {
                title: '任务ID',
                field: 'id',
                align: 'center',
                valign: 'middle'
            },
            {
                  title: '任务类型',
                  field: 'type',
                  align: 'center',
                  valign: 'middle'
            },
            {
                  title: '任务进度',
                  field: 'progress',
                  align: 'center'
            },
            {
                  title: '任务状态',
                  field: 'status',
                  align: 'center'
            },
            {
                  title: '开始时间',
                  field: 'start_time',
                  align: 'center'
            },
            {
                  title: '结束时间',
                  field: 'end_time',
                  align: 'center'
            },
            {
                  title: '操作',
                  align: 'center',
                  formatter:function(value,row,index){
                      var read = '<button type="button" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#portattackchild_dialog" onclick="portattackchild_read(\''+ row.id + '\')">查看</button> ';
                      var stop = '<button type="button" class="btn btn-warning btn-xs" onclick="port_attack_pause(\''+ row.id + '\' , \'' +row.status + '\')">暂停</button> ';
                      // 该功能暂时不用。
                      //var restart = '<button type="button" class="btn btn-warning btn-xs" onclick="port_attack_restart(\''+ row.id + '\' , \'' +row.status + '\')">&nbsp;&nbsp;&nbsp;&nbsp;</button> ';
                      var restart = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
                      var start = '<button type="button" class="btn btn-warning btn-xs" onclick="port_attack_start(\''+ row.id + '\' , \'' +row.status + '\')">启动</button> ';
                      var del = '<button type="button" class="btn btn-danger btn-xs" onclick="port_attack_del(\''+ row.id + '\' , \'' +row.status + '\')">删除</button> ';
                      if (row.status == "pause"){
                          return read+start+del;
                      } else if (row.status == "running"){
                          return read+stop+del;
                      } else {
                          return read+restart+del;
                      }
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
    $('#cms_scan_table').bootstrapTable({
        url: "/AnyScanUI/cms_scan_list/",
        method:"post",
        dataType: "json",
        pagination: true, //分页
        contentType: "application/x-www-form-urlencoded",
        singleSelect: false,
        search: true, //显示搜索框
        striped: true,  //表格显示条纹
        pagination: true, //启动分页
        pageSize: 10,  //每页显示的记录数
        pageNumber:1, //当前第几页
        pageList: [10, 20, 30, 40],  //记录数可选列表
        showRefresh:true,
        //toolbar: '#port_attack_toolbar',
        columns: [
            {
                  title: 'ID',
                  field: 'id',
                  align: 'center',
                  valign: 'middle',
                  visible:false,
                  width:0
            },
            {
                  title: '主机/域名',
                  field: 'host',
                  align: 'center',
                  valign: 'middle'
            },
            {
                  title: '扫描状态',
                  field: 'status',
                  align: 'center'
            },
            {
                  title: '扫描进度',
                  field: 'progress',
                  align: 'center'
            },
            {
                  title: '线程数',
                  field: 'threads',
                  align: 'center'
            },
            {
                  title: 'CMS',
                  field: 'cms',
                  align: 'center'
            },
            {
                  title: '版本',
                  field: 'version',
                  align: 'center'
            },
            {
                  title: '荷载',
                  field: 'payload',
                  align: 'center'
            },
            {
                  title: '关键字/MD5',
                  field: 'keyword',
                  align: 'center'
            },
            {
                  title: '操作',
                  align: 'center',
                  formatter:function(value,row,index){
                      var stop = '<button type="button" class="btn btn-warning btn-xs" onclick="cms_scan_stop_func(\''+ row.id + '\' , \'' +row.status + '\')">暂停</button> ';
                      var del = '<button type="button" class="btn btn-danger btn-xs" onclick="cms_scan_del_func(\''+ row.id + '\' , \'' +row.status + '\')">删除</button> ';
                      return stop+del;
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
    // 初始化端口爆破任务，子任务列表
    $('#port_attack_list').bootstrapTable({
        url: "/AnyScanUI/portattackchild_list/",
        method:"post",
        //data:[{"status": "running", "end_time": "2017-02-27 02:37:45", "ip": "10.42", "progress": "10.42%", "start_time": "2017-02-27 02:36:22", "type": "SSH", "id": "870161e6-fc95-11e6-bd7d-784f435e6bbf", "port": "10.42"}, {"status": "success", "end_time": "2017-02-27 02:37:21", "ip": "100", "progress": "100%", "start_time": "2017-02-27 02:36:22", "type": "SSH", "id": "8702e175-fc95-11e6-9d4e-784f435e6bbf", "port": "100"}],
        dataType: "json",
        pagination: true, //分页
        contentType: "application/x-www-form-urlencoded",
        singleSelect: false,
        search: true, //显示搜索框
        striped: true,  //表格显示条纹
        pagination: true, //启动分页
        pageSize: 10,  //每页显示的记录数
        pageNumber:1, //当前第几页
        pageList: [10, 20, 30, 40],  //记录数可选列表
        //showRefresh:true,
        toolbar: '#port_attacklist_toolbar',
        columns: [
            {
                  title: 'IP/HOST',
                  field: 'ip',
                  align: 'center',
                  valign: 'middle'
            },
            {
                  title: 'PORT',
                  field: 'port',
                  align: 'center',
                  valign: 'middle'
            },
            {
                  title: '任务类型',
                  field: 'type',
                  align: 'center'
            },
            {
                  title: '进度',
                  field: 'progress',
                  align: 'center'
            },
            {
                  title: '线程',
                  field: 'threads',
                  align: 'center'
            },
            {
                  title: '任务状态',
                  field: 'status',
                  align: 'center'
            },
            {
                  title: '用户名',
                  field: 'username',
                  align: 'center'
            },
            {
                  title: '密码',
                  field: 'password',
                  align: 'center'
            },
            {
                  title: '开始时间',
                  field: 'start_time',
                  align: 'center'
            },
            {
                  title: '结束时间',
                  field: 'end_time',
                  align: 'center'
            }
        ],
        onLoadSuccess:function(data){
            //alert(JSON.stringify(data));
        },
        onLoadError:function(data){
            //alert(data);
        }
    });

    $('#poc_exec_task_table').bootstrapTable({
        url: "/AnyScanUI/poc_main_list/",
        method:"post",
        dataType: "json",
        pagination: true, //分页
        contentType: "application/x-www-form-urlencoded",
        singleSelect: false,
        search: true, //显示搜索框
        striped: true,  //表格显示条纹
        pagination: true, //启动分页
        pageSize: 10,  //每页显示的记录数
        pageNumber:1, //当前第几页
        pageList: [10, 20, 30, 40],  //记录数可选列表
        showRefresh:true,
        //toolbar: '#port_attack_toolbar',
        columns: [
            {
                title: '任务ID',
                field: 'id',
                align: 'center',
                visible:false,
                valign: 'middle'
            },
            {
                  title: 'URL采集命令',
                  field: 'commond',
                  align: 'center',
                  valign: 'middle'
            },
            {
                  title: '任务进度',
                  field: 'progress',
                  align: 'center'
            },
            {
                  title: '线程',
                  field: 'threads',
                  align: 'center'
            },
            {
                  title: '任务状态',
                  field: 'status',
                  align: 'center'
            },
            {
                  title: '开始时间',
                  field: 'start_time',
                  align: 'center'
            },
            {
                  title: '结束时间',
                  field: 'end_time',
                  align: 'center'
            },
            {
                  title: '操作',
                  align: 'center',
                  formatter:function(value,row,index){
                      var read = '<button type="button" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#poc_chil_dialog" onclick="poc_chil_list(\''+ row.id + '\')">查看</button> ';
                      return read;
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

    // poc执行子任务列表
    $('#poc_chil_table').bootstrapTable({
        url: "/AnyScanUI/poc_chil_list/",
        method:"post",
        dataType: "json",
        pagination: true, //分页
        contentType: "application/x-www-form-urlencoded",
        singleSelect: false,
        search: true, //显示搜索框
        striped: true,  //表格显示条纹
        pagination: true, //启动分页
        pageSize: 10,  //每页显示的记录数
        pageNumber:1, //当前第几页
        pageList: [10, 20, 30, 40],  //记录数可选列表
        showRefresh:true,
        //toolbar: '#port_attack_toolbar',
        columns: [
            {
                title: '任务ID',
                field: 'id',
                align: 'center',
                visible:false,
                valign: 'middle'
            },
            {
                  title: '域名/IP',
                  field: 'host',
                  align: 'center',
                  valign: 'middle'
            },
            {
                  title: 'URL采集命令',
                  field: 'commond',
                  align: 'center',
                  valign: 'middle'
            },
            {
                  title: '有无漏洞',
                  field: 'vulnerable',
                  align: 'center'
            },
            {
                  title: '验证结果',
                  field: 'keyword',
                  align: 'center'
            }
        ],
        onLoadSuccess:function(data){
            //alert(JSON.stringify(data));
        },
        onLoadError:function(data){
            //alert(data);
        }
    });

    /**
     * sqlmap扫描停止按钮绑定事件
     */
    $("#kill").click(function(){
        // 清除前台的日志轮训查询任务
        clearInterval(readlogInterval);
        // 停止扫描任务
        clearInterval(kill_flag);
        // stop掉后台的扫描任务
        stop(taskids);
        $("#bash").removeClass('disabled');
        $("#start").removeClass('disabled');
    });

    /**
     * sqlmap扫描任务开始按钮绑定事件
     */
    $("#start").click(function(){
        // sqlmap 参数对象
        var data = {};
        // 用户输入的sqlmap语句
        var url = $("#url").val()
        //url = "sqlmap -u http://192.168.1.185:8099/test.php?id=1 --random-agent --tamper=versionedmorekeywords  --dbms=mysql  --is-dba --tables --current-user --current-db --passwords --union-char=1 --threads=2";
        // 分解sqlmap命令
        var url_ = url.split(" ");
        // 去掉sqlmap单词
        url_.splice(0,1);
        // sqlmap和sqlmapapi语法对应关系字典的key
        var key_ = "";
        // sqlmap和sqlmapapi语法对应关系字典的value
        var value_ = "";
        // sqlmap和sqlmapapi语法对应关系字典
        var param_dic = {"u":"url","random-agent":"randomAgent","users":"getUsers","is-dba":"isDba","tables":"getTables","dbs":"getDbs",
                        "columns":"getColumns","level":"level","tamper":"tamper","no-cast":"noCast","outtime":"timeout","time-sec":"timeSec",
                        "dbms":"dbms","current-user":"getCurrentUser","current-db":"getCurrentDb","passwords":"getPasswordHashes",
                        "union-char":"uChar","cookie":"cookie","data":"data","threads":"threads","ttbl":"tbl",
                        "ddb":"db","ttbl":"tbl","ccol":"col","uuser":"user","d":"db","t":"tbl","c":"col",};

        // 匹配格式 --random-agent 类型
        var reg___ = /^\-\-[a-zA-Z]+\-[a-zA-Z]+/;
        // 匹配 --tables 类型
        var reg__ = /^\-\-[a-zA-Z]/;
        // 匹配 -u 类型
        var reg_ = /^\-[a-zA-Z]/;
        // 匹配 --level=2 类型
        var reg = /^\-\-[a-zA-Z]+\=[\s\S]+/;
        // 匹配 --union-char=1
        var res = /^\-\-[a-zA-Z]+\-[a-zA-Z]+\=[\s\S]/;

        var index_ = 0;
        // 循环解析用户输入的sqlmap语句，将其解释为sqlmapapi所支持的关键字语法。
        while (index_ < url_.length){
            var t = url_[index_];
            if (t == "" || t == undefined){
                index_+=1;
                continue;
            }
            var key_ = "";
            var value_ = "";
            // 正则匹配语法
            if(t.match(res)){
                key_ = t.substring(2, t.indexOf("="));
                value_ = t.substring(t.indexOf("=")+1, t.length);
                index_+=1;
            } else if(t.match(reg___)){
                key_ = t.substring(2, t.length);
                value_ = true;
                index_+=1;
            } else if(t.match(reg)){
                key_ = t.substring(2, t.indexOf("="));
                value_ = t.substring(t.indexOf("=")+1, t.length);
                index_+=1;
            } else if(t.match(reg__)){
                key_ = t.substring(2, t.length);
                value_ = true;
                index_+=1;
            } else if(t.match(reg_)){
                key_ = t.substring(1, t.length);
                value_ = url_[index_+1];
                index_+=2;
            } else {
                index_ += 1;
                continue;
            }
            data[param_dic[key_.toLowerCase()]] = value_;
        }
        //alert(JSON.stringify(data));
        start(data);
        // 按钮禁用
        $("#bash").addClass('disabled');
        $("#start").addClass('disabled');
    });
    /**
     * 检测绕过按钮事件绑定
     */
    $("#bash").click(function(){
        var data = {"url":$("#url").val(),"bash":"1"};
        start(data);
        $("#bash").addClass('disabled');
        $("#start").addClass('disabled');
    });
    /**
     * 扫描任务列表中，日志弹框的关闭事件
     */
    $('#task_log').on('hidden.bs.modal', function (e) {
        clearInterval(readlogInterval);
    });
    /**
     * 扫描任务列表中的清空按钮绑定事件
     */
    $('#flush').click(function(){
        $.ajax({
            type: 'POST',
            url: "/AnyScanUI/web_flush/",
            data: JSON.stringify({}),
            success: function(data, status){
                $('#overview').bootstrapTable('refresh');
            },
            dataType: "json"
        });
    });
    // nmap日志刷新变量
    var logwating;
    // 端口扫描按钮事件
    $('#port_scan_start').click(function(){
        var commond = $("#port_scan_commond").val();
        if (commond == "" || commond == null){
            alert("请输入扫描命令！");
            return;
        }
        $("#port_scan_start").addClass('disabled');
        $("#port_burp_start").removeClass('disabled');
        $.fn.zTree.init($("#portscan_tree"), init_ztree(), [{"id":"1","name":"Port Scan Result","children":[]}]);
        var count = 0;
        logwating = setInterval(function () {
            count+=1;
            $("#port_scan_log").html("NMap扫描进度不能实时显示，所以请稍后。当前用时[" + count + "]秒。");
        }, 1000);
        var data = {"host":"","port":"","arguments":""}

        //commond = "nmap -p1-65535 -T4 -A -v -Pn 127.0.0.1";
        var commonds = commond.split(" ");
        var reg_port = /^\-p\d{0,5}\-\d{0,5}/;
        var reg_port_= /^\-p\d{0,5}(,\d{0,5})*/;
        var tmp;
        var tmp_;
        // 解析-p参数
        $.each(commonds, function(index, value){
            tmp = value.match(reg_port);
            tmp_ = value.match(reg_port_);
            if (tmp || tmp_){
                data.port = value.replace("-p", "");
            }
        });
        data.host = commonds[commonds.length-1];
        data.arguments = commond.replace(data.host,"").replace("-p"+data.port,"").replace("nmap","");
        var log = "";
        // nmap扫描请求
        $.ajax({
            type: 'POST',
            url: "/AnyScanUI/port_scaner/",
            data: JSON.stringify(data),
            //timeout:1000, //超时时间设置，单位毫秒
            success: function(data, status){
                clearInterval(logwating);
                $("#port_scan_start").removeClass('disabled');
                log = read_file(data);
                port_scan_tree = $.fn.zTree.init($("#portscan_tree"), init_ztree(), eval("("+data["port_scan_json_data"]+")"));
            },
            error: function(data,status){
                alert(JSON.stringify(data));
                clearInterval(logwating);
                $("#port_scan_start").removeClass('disabled');
                $("#port_scan_log").html("扫描失败。用时[" + count + "]秒。");
            },
            dataType: "json"
        });

    });

    var zTree;
    var nodes = [{name: "Port Scan Result"}];
    $.fn.zTree.init($("#portscan_tree"), init_ztree(), nodes);

    /**
     * 端口暴力破解按钮事件
     */
    $('#port_burp_start').click(function(){
        current_port_attack_status = "running";
        $("#port_burp_start").addClass('disabled');
        port_attack_success_num = 0;
        clearInterval(attackportlogInterval);
        var treeObj = $.fn.zTree.getZTreeObj("portscan_tree");
        var nodes = treeObj.getCheckedNodes(true);
        // data = {"ip":[80,3306]}
        var data_ = {};
        $.each(nodes, function(index, value) {
            if (value["scanning"] == "true" || value["scanning"] == true){
                if (data_[value["ip"]] == null || data_[value["ip"]] == undefined || data_[value["ip"]] == ""){
                    data_[value["ip"]] = [value["port"]]
                }else{
                    data_[value["ip"]].push(value["port"])
                }
            }
        });

        if (Object.getOwnPropertyNames(data_).length < 1){
            alert("请勾选您要爆破的对象");
            $("#port_burp_start").removeClass('disabled');
            return;
        }
        var threads = $("#port_burp_threads").val();
        var re_num = /^[0-9]*$/;
        if(!re_num.test(threads)){
            alert("线程数只能为数字");
            return;
        }
        if (threads > 100){
            alert("线程数最多为100");
            return;
        }
        var data__ = {"attack_dict":data_,"threads":threads,"type":"create"}
        // 根据用户选择的端口调用方法进行暴力破解
        $.ajax({
            type: 'POST',
            url: "/AnyScanUI/portattack/",
            data: JSON.stringify(data__),
            success: function(data, status){
                current_port_attack_id = data["logid"];
                if(data["status"] == true) {
                    attackportlogInterval = setInterval(function () {
                        portattack_log(self,data["logid"]);
                    }, 2000);

                }else{
                    $("#port_burp_start").removeClass('disabled');
                    $("#port_scan_log").html(data["data"]);
                    // 记录当前暴力破解任务的id
                    current_port_attack_id = "";
                    // 记录当前爆破任务的状态
                    current_port_attack_status = "pause";
                }
            },
            dataType: "json"
        });
    });

    /**
     * 暂停当前爆破任务
     */
    $('#port_burp_stop').click(function() {
        if (current_port_attack_id == "" || current_port_attack_id == null){
            alert("当前没有任务可以暂停！");
            return;
        }
        if (current_port_attack_status == "pause"){
            alert("当前已被暂停！");
            return;
        }
        current_port_attack_status = "pause";
        port_attack_success_num = 0;
        clearInterval(attackportlogInterval);
        port_attack_pause(current_port_attack_id,"running")
        $("#port_burp_start").removeClass('disabled');
        $("#port_scan_log").html("爆破任务被暂停！\n" +$("#port_scan_log").html())
    });

    // 爆破子任务列表
    $('#port_attacklist_refresh').click(function() {
        refresh_portattackchild(portattackid);
    });

    // CMS识别按钮事件
    $('#cms_start').click(function() {
        clearInterval(cms_scan_log_interval);
        var cms_url = $("#cms_url").val();
        if (cms_url == "" || cms_url == null) {
            alert("请输入检测网址！");
            return;
        }
        $("#cms_start").addClass('disabled');
        $("#cms_stop").removeClass('disabled');
        var data = {"url":cms_url};
        $.ajax({
            type: 'POST',
            url: "/AnyScanUI/cms_scan/",
            data: JSON.stringify(data),
            //timeout:1000, //超时时间设置，单位毫秒
            success: function(data, status){
                //clearInterval(logwating);
                cms_scan_ids = data["ids"];
                // 轮询查询cms识别日志
                cms_scan_log(cms_scan_ids);
            },
            error: function(data,status){
                clearInterval(cms_scan_log_interval);
                $("#cms_start").removeClass('disabled');
                $("#cms_logging").html(data["data"]);
            },
            dataType: "json"
        });
    });
    // CMS识别按钮事件
    $('#cms_stop').click(function() {
        $("#cms_start").removeClass('disabled');
        clearInterval(cms_scan_log_interval);
        $.ajax({
            type: 'POST',
            url: "/AnyScanUI/cms_scan_stop/",
            data: JSON.stringify({"ids":cms_scan_ids}),
            //timeout:1000, //超时时间设置，单位毫秒
            success: function(data, status){
                var h = $("#cms_logging").html();
                $("#cms_logging").html("任务被停止\n" + h);
            },
            dataType: "json"
        });
    });

    var pocObj = CodeMirror.fromTextArea(document.getElementById("code-python"), {
        mode: {name: "text/x-cython",
               version: 2,
               singleLineStringErrors: false},
        lineNumbers: true,
        indentUnit: 4,
        matchBrackets: true,
        autofocus:false

    });

    // poc执行按钮事件绑定
    $('#exec_poc').click(function() {
        var commond = $("#search_content").val();
        var targets = poc_targets();
        var payload = pocObj.getValue();

        if (targets.length < 1){
            alert("请勾选要测试的URL！");
            return;
        }
        $("#exec_poc").addClass('disabled');
        var data = {"targets":targets,"payload":payload,"commond":commond};
        $.ajax({
            type: 'POST',
            url: "/AnyScanUI/exe_poc/",
            data: JSON.stringify(data),
            //timeout:1000, //超时时间设置，单位毫秒
            success: function(data, status){
                poc_exec_log_interval = setInterval(function () {
                    poc_exec_log(data);
                }, 1000);
            },
            dataType: "json"
        });
    });
    $("#url_google").addClass('disabled');
    // url采集树
    var url_list_node = [{name: "Url Result"}];
    $.fn.zTree.init($("#url_list_tree"), init_ztree(), url_list_node);
    var url_list_tree = $.fn.zTree.getZTreeObj("url_list_tree");

    // 百度url采集事件绑定
    $('#url_baidu').click(function() {
        $("#url_baidu").addClass('disabled');
        var commond = $("#search_content").val();

        var data = {"commond":commond};
        $.ajax({
            type: 'POST',
            url: "/AnyScanUI/baidu_url/",
            data: JSON.stringify(data),
            //timeout:1000, //超时时间设置，单位毫秒
            success: function(data, status){
                //$.fn.zTree.init($("#url_list_tree"), init_ztree(), data);
                poc_url_interval = setInterval(function () {
                    poc_url_log(data);
                }, 1000);
            },
            dataType: "json"
        });
    });
});

/**
 *
 * @returns {Array}
 */
function poc_targets(){
    var treeObj = $.fn.zTree.getZTreeObj("url_list_tree");
    var nodes = treeObj.getCheckedNodes(true);

    var targets = [];
    for(var i = 0; i < nodes.length; i++){
        var node = nodes[i];
        if (node["url"] != null && node["url"] != "" && node["url"] != undefined){
            targets.push(node["url"]);
        }
    }
    return targets;
}

/**
 * 更新POC执行日志
 * @param data
 */
function poc_exec_log(data){
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/exec_poc_log/",
        data: JSON.stringify({"id":data["id"]}),
        success: function(data, status){
            $("#poc_url_log").html(data["log"]);
            if (data["status"] == "False" || data["status"] == false){
                $("#url_baidu").removeClass('disabled');
                //$("#url_google").removeClass('disabled');
                $("#exec_poc").removeClass('disabled');
                clearInterval(poc_exec_log_interval);
            }
            if (data["log_status"] != "running"){
                $("#url_baidu").removeClass('disabled');
                //$("#url_google").removeClass('disabled');
                $("#exec_poc").removeClass('disabled');
                clearInterval(poc_exec_log_interval);
            }
        },
        dataType: "json"
    });
}

/**
 * 更新url树，更新日志内容
 * @param data
 */
function poc_url_log(data){
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/url_log/",
        data: JSON.stringify({"id":data["id"]}),
        success: function(data, status){
            var zTreeObj = $.fn.zTree.getZTreeObj("url_list_tree");
            zTreeObj.destroy();
            $.fn.zTree.init($("#url_list_tree"), init_ztree(), data["data"]);
            $("#poc_url_log").html(data["log"]);
            if (data["status"] == "False" || data["status"] == false){
                $("#url_baidu").removeClass('disabled');
                clearInterval(poc_url_interval);
            }
            if (data["log_status"] != "running"){
                $("#url_baidu").removeClass('disabled');
                clearInterval(poc_url_interval);
            }
        },
        dataType: "json"
    });
}

/**
 * sqlmap扫描任务开始方法
 * @param data 扫描任务参数
 */
function start(data){
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/bash_task/",
        data: JSON.stringify(data),
        success: function(data, status){
            // 获取返回的taskid
            taskids = data["taskid"]
            if(data["success"] == true){
                kill_flag = setInterval(function(){
                    web_log("logging",data);
                },1000);
            }
        },
        dataType: "json"
    });
}
/**
 * 扫描任务停止
 * @param taskid 任务id
 */
function stop(taskid){
    data = {"taskid":taskid};
    if(typeof(taskid) == "string"){
        data = {"taskid":[taskid]};
    }
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/task_stop/",
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
/**
 * 删除扫描任务
 * @param taskid 任务id
 */
function del_task(taskid){
    data = {"taskid":taskid};
    if(typeof(taskid) == "string"){
        data = {"taskid":[taskid]};
    }
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/web_delete/",
        data: JSON.stringify(data),
        success: function(data, status){
            $('#overview').bootstrapTable('refresh');
            //alert(data["msg"]);
        },
        error: function(data){
            //$("#errotext").val(data["msg"]);
            alert(JSON.stringify(data));
        },
        dataType: "json"
    });
}

/**
 * 读取sqlmap扫描日志
 * @param taskid 任务ID
 * @param status 任务状态
 */
function read(taskid,status){
    // 只有扫描任务为running时，才实时刷新日志
    if (status == "running") {
        readlogInterval = setInterval(function () {
            web_log("read_logging", {"taskid": taskid});
        }, 1000);
    }else {
        web_log("read_logging", {"taskid": taskid});
    }
}

/**
 * 读取sqlmap扫描日志
 * @param logid 显示日志的页面控件id
 * @param data 请求参数
 */
function web_log(logid,data){
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/web_log/",
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

/**
 * 读取cms识别日志
 * @param ids id列表
 */
function cms_scan_log(ids){
    // 只有扫描任务为running时，才实时刷新日志
    cms_scan_log_interval = setInterval(function () {
        cms_scan_log_fuc(ids);
    }, 1000);
}
/**
 * 读取cms识别日志
 * @param ids cms识别任务id
 */
function cms_scan_log_fuc(ids){

    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/cms_scan_log/",
        data: JSON.stringify({"ids":ids}),
        success: function(data, status){
            if (data["status"] == false || data["status"] == "false"){
                clearInterval(cms_scan_log_interval);
                $("#cms_start").removeClass('disabled');
            }
            if (data["success"] == "success"){
                clearInterval(cms_scan_log_interval);
                $("#cms_start").removeClass('disabled');
                $("#cms_logging").html("CMS识别完成\n"+data["data"]);
            }
            $("#cms_logging").html(data["data"]);
        },
        dataType: "json"
    });
}

/**
 * 读取服务器文件
 * @param path 文件路径
 */
function read_file(portscan_data){
    var data = {"port_scan_filepath":portscan_data["port_scan_filepath"]};
    var log = "";
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/read_file/",
        data: JSON.stringify(data),
        success: function(data, status){
            log = data.data;
            $("#port_scan_log").html(log);
        },
        dataType: "json"
    });
    return log;
}

/**
 * ztree配置初始化
 **/
function init_ztree(){
    var setting = {
        view: {
            dblClickExpand: false,
            showLine: true,
            selectedMulti: false
        },
        data: {
            simpleData: {
                enable: true,
                idKey: "id",
                pIdKey: "pId",
                rootPId: ""
            }
        },
        check: {
            enable: true
        },
        callback : {
		    //onRightClick : zTreeOnRightClick
        }
    };
    return setting
}

/**
 * 读取port爆破日志
 * @param logid logid
 */
function portattack_log(self_,logid){
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/portattacklog/",
        data: JSON.stringify({"logid":logid}),
        success: function(data, status){
            if (data["attack_status"] == "pause"){
                data["data"] = "爆破任务被暂停！\n" + data["data"]
            }
            if (data["attack_status"] == "success"){
                data["data"] = "爆破任务完成！\n" + data["data"]
            }
            $("#port_scan_log").html(data["data"]);

            if (data["status"] == true){
                var result = data["result"];
                changetreestatus(result);
            }
            // 如果爆破完成，清除轮询
            if (data["attack_status"] == "pause" || data["status"] == false ){
                $("#port_burp_start").removeClass('disabled');
                clearInterval(attackportlogInterval);
            }
            if (data["attack_status"] == "success"){
                port_attack_success_num += 1;
            }
            // 连续成功三次清除轮询，防止延时
            if (port_attack_success_num == 3 ){
                $("#port_burp_start").removeClass('disabled');
                port_attack_success_num = 0;
                clearInterval(attackportlogInterval);
                //alert("爆破完成");
            }
        },
        dataType: "json"
    });
}

/**
 * 更新端口树的状态
 * @param result
 */
function changetreestatus(result){
    result = eval("("+result+")");
    var treeObj = $.fn.zTree.getZTreeObj("portscan_tree");
    var nodes = treeObj.getCheckedNodes(true);
    var data_ = {};

    for(var i = 0; i < nodes.length; i++){
        var node = nodes[i];
        if (node["scanning"] == "true" || node["scanning"] == true){
            for(var j = 0; j < result.length; j++){
                var resulter = result[j];
                //if (node["ip"] == resulter["ip"] && node["port"] == resulter["port"] && node["mark"] != "true"){
                if (node["ip"] == resulter["ip"] && node["port"] == resulter["port"]){
                    if (resulter["username"] != "" || resulter["username"] != null) {
                        var __name = nodes[i]["name"]
                        __name = __name.split("【");
                        nodes[i]["name"] = __name[0] + "【" + resulter["username"] + ":" + resulter["password"] + "】";
                        // 标记该条目已经更新过用户名密码，不需要再次更新。
                        nodes[i]["mark"] = "true";
                        treeObj.updateNode(nodes);
                        treeObj.refresh();
                        break;
                    }
                }
            }
        }
    }
}

/**
 * 端口爆破任务暂停
 * @param id
 */
function port_attack_pause(id,status){
    // 判断当前任务状态，如果任务被暂停，不发送ajax
    if (status != "running"){
        alert("当前任务已停止，不可暂停！");
        return;
    }
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/portattackpause/",
        data: JSON.stringify({"id":id}),
        success: function(data, status){
            $('#port_attack_table').bootstrapTable('refresh');
        },
        dataType: "json"
    });
}

/**
 * 端口爆破任务启动，由暂停变为启动
 * @param id
 */
function port_attack_start(id,status){
    // 判断当前任务状态，如果任务被暂停，不发送ajax
    if (status == "running"){
        alert("当前任务正在运行，无需启动！");
        return;
    }
    if (status == "finish" || status == "success"){
        alert("当前任务已结束，无法启动！");
        return;
    }
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/portattack/",
        data: JSON.stringify({"id":id,"type":"start"}),
        success: function(data, status){
            $('#port_attack_table').bootstrapTable('refresh');
        },
        dataType: "json"
    });
}

/**
 * 端口爆破任务重新启动，由失败变为启动
 * @param id
 */
function port_attack_restart(id,status){
    // 空白函数
    alert("未实现该函数！");
    return;
}

/**
 * 端口爆破任务删除
 * @param id
 * @status 状态
 */
function port_attack_del(id,status){
    // 判断当前任务状态，如果任务被暂停，不发送ajax
    if (confirm("删除后不可恢复，你确定要删除吗？")) {
        $.ajax({
            type: 'POST',
            url: "/AnyScanUI/portattackdel/",
            data: JSON.stringify({"id":id}),
            success: function(data, status){
                if (data["status"] == false || data["status"] == "false"){
                    alert(data["msg"]);
                }
                $('#port_attack_table').bootstrapTable('refresh');
            },
            dataType: "json"
        });
    } else {
        alert("点击了取消");
    }

}

/**
 * 获取爆破任务的子任务
 * @param id 任务ID
 */
function portattackchild_read(id){
    portattackid = id;
    // 获取扫描任务
    refresh_portattackchild(id);
}

function refresh_portattackchild(id){
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/portattackchild_list/",
        data: JSON.stringify({"id":id}),
        success: function(data, status){
            if (data["status"] == false || data["status"] == "false"){
                alert(data["msg"]);
                return;
            }
            $("#port_attack_list").bootstrapTable('load',data["rows"]);
        },
        dataType: "json"
    });
}
/**
 * 获取POC执行子任务
 * @param id
 */
function poc_chil_list(id){
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/poc_chil_list/",
        data: JSON.stringify({"id":id}),
        success: function(data, status){
            if (data["status"] == false || data["status"] == "false"){
                alert(data["msg"]);
                return;
            }
            $("#poc_chil_table").bootstrapTable('load',data["rows"]);
        },
        dataType: "json"
    });
}

/**
 * CMS识别任务停止
 * @param id
 */
function cms_scan_stop_func(id,status){
    // 判断当前任务状态，如果任务被暂停，不发送ajax
    if (status != "running"){
        alert("当前任务不是运行状态，不可暂停！");
        return;
    }
    $.ajax({
        type: 'POST',
        url: "/AnyScanUI/cms_scan_stop/",
        data: JSON.stringify({"ids":[id]}),
        success: function(data, status){
            $('#cms_scan_table').bootstrapTable('refresh');
        },
        dataType: "json"
    });
}

/**
 * CMS识别任务删除
 * @param id
 * @status 状态
 */
function cms_scan_del_func(id,status){
    if (confirm("删除后不可恢复，你确定要删除吗？")) {
        $.ajax({
            type: 'POST',
            url: "/AnyScanUI/cms_scan_del/",
            data: JSON.stringify({"id":id}),
            success: function(data, status){
                if (data["status"] == false || data["status"] == "false"){
                    alert(data["msg"]);
                }
                $('#cms_scan_table').bootstrapTable('refresh');
            },
            dataType: "json"
        });
    } else {
    }

}