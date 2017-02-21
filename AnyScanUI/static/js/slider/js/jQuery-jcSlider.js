/*
 * jQuery - jcSlider v1.43
 * Copyright(c) 2012 by Riddick-design 
 * Date: 2012-01-02
 */
;(function($){
	$.fn.jcSlider = function(options) {
		var defaults = {
			loading:true,                 //预加载loading开关设置，提供true,false
			loadpic:'img/loading.gif',     //预加载loading图片路径，相对定位,如../img/riddick.png
			play:true,                     //是否开起自动播放功能，提供true,false
			play_speed:1500,               //自动播放速度设置，提供easing值 或 数值(mm)
			slider_btn:true,               //左右按钮开关，提供true,false
			slider_speed:500,              //图片切换速度设置，提供easing值 或 数值(mm)
			slider_num:true,               //数字按钮开关，提供true,false
			offset:40,                      //设置左右按钮偏移量(px)
			btn_event:'click',             //数字按钮事件设置，提供click,mouseover等
			btn_position:'middle',         //数字按钮位置，提供left,middle,right
			num_offsetW:0,                 //设置数字按钮的X偏移(px)
			num_offsetH:330,               //设置数字按钮的Y偏移(px)
			scaling:true,                  //是否设置图片大小，提供true,false
			width:956,                     //设置图片宽度单位(px)
			height:300,                    //设置图片高度单位(px)
			sliderModle:'xScroll'          //设置slider显示模式，提供fade，xScroll
		};
		var options = $.extend(defaults,options);
		return this.each(function() {
            var $wrap = $(this),
			    _ind = 0,
				xx =0,
				$wrap_ul = $wrap.find('ul'),
				$wrap_li = $wrap_ul.children('li'),
				$html = {
				    tNum : "<ul id='sliderNum'></ul>",
					tLoadPic : "<img src=\""+options.loadpic+"\" class=\"loadpic\">",
					tpicHide : "<div id='picHide'></div>",
					tSliderBtn : "<a id='slider_prev'></a><a id='slider_next'></a>"
				};
	    	$wrap.append($html.tNum);
			/* overflow BUG 修正 */	
			$wrap_ul.filter(':eq(0)')
			        .wrap($html.tpicHide);
			var $wrap_img = $wrap.find('#picHide')
			                     .children('ul:eq(0)')
								 .find('img'),
			    $picHide = $('#picHide',$wrap);
			$picHide.css({ 'left':($wrap.width()-$picHide.width())/2+'px',
						   'top':($wrap.height()-$picHide.height())/2+'px'
					    });
			/* 图片缩放 */
			if(options.scaling === true){
            	$wrap_img.attr({'width':options.width,'height':options.height});
			};
            /* 图片预加载 */
		    if( options.loading === true ){
				_loading=$($html.tLoadPic);
				$wrap_img.hide();
				$wrap_img.after(_loading);
				var $loadpic = $('.loadpic',$wrap_li);
				$loadpic.css({ 'position':'relative',
							   'left':($wrap.width()-$loadpic.width())/2-20,
							   'top':($wrap.height()-$loadpic.height())/2
							});
				$wrap_img.each(function(){
			        $wrap_img.load(function(){
                        _loading.hide();
                        $(this).fadeIn(options.slider_speed);
		            });
				});
		    };
			/* slider展示模式 */
			function sliderMod(ind) {
				switch(options.sliderModle){
                    case 'fade':
						$wrap_li.stop()
						        .fadeOut(options.slider_speed)
								.eq(ind)
								.fadeIn(options.slider_speed);
						break;
                    case 'xScroll':
						$wrap_ul.eq(0)
							    .stop()
							    .animate({ left: -(ind*$wrap_li.width()) 
									  }, options.slider_speed);
						break;
				};
				_ind = ind;
			};
			/* slider数字按钮 */
			if(options.slider_num === true) {
				var $num = $('#sliderNum',$wrap);
			    $wrap_li.each(function(index){		
			        var _number = index+1;
                    $num.append('<li>'+_number+'</li>');	
			    });
				var $numLi = $num.find('li');
				$numLi.eq(0).addClass('visited');
				var _numW = $num.width();
				switch(options.btn_position){
                    case 'left':
                        _btn_position = ($wrap.width()-_numW)*0;
					    break;
                    case 'middle':
                        _btn_position = ($wrap.width()-_numW)/2;
					    break;
                    case 'right':
                        _btn_position = ($wrap.width()-_numW);
					    break;
				};
			    var N_left = _btn_position
				$num.css({ "left":N_left+options.num_offsetW,
						   'top':options.num_offsetH 
						});
				/* 数字按钮切换图片 */
             	$num.delegate('li',options.btn_event,function(){ 
                    $index = $numLi.index($(this));
					sliderMod($index);
                    $(this).addClass('visited').siblings().removeClass('visited');
                    _ind = $index;
            	});
		    };
			/* slider左右按钮 */
		    if(options.slider_btn === true) {
				$wrap.append($html.tSliderBtn);
				var $next = $('#slider_next',$wrap),
				    $prev = $('#slider_prev',$wrap);
                $next.css({ 'left':$wrap.width()-$next.width()+options.offset,
							'top':($wrap.height()-$next.height())/2
						 });
                $prev.css({ 'left':-options.offset,
						    'top':($wrap.height()-$prev.height())/2
						 });
				/* slider左右按钮切换图片 */
				function next_btn(){
				    if( _ind < $wrap_li.length-1 ) {
		                _ind++;
		            } else {
	                    _ind = 0;
		            };
					sliderMod(_ind);
		            $numLi.removeClass('visited');
		            $numLi.eq(_ind).addClass('visited');
					return false;
				}
				function prev_btn(){
					if( _ind >= 1 ) {
		                _ind--;
		            } else {
		                _ind = $wrap_li.length-1;
		            };
					sliderMod(_ind);
	                $numLi.removeClass('visited');
	                $numLi.eq(_ind).addClass('visited');
					return false;
				}
                $wrap.delegate('a#slider_next','click',function(){ 
                    next_btn();
                });
                $wrap.delegate('a#slider_prev','click',function(){
                    prev_btn();
                });
                /* 键盘操作 */
                $(window).keydown(function(e){
			        var key = e.keyCode?e.keyCode:e.which;
			        switch(key) {
			            case 39: 
			                next_btn();
			                break;
			            case 37:
			                prev_btn();
			                break;
			        }
			        return;
                });
		    };
			/* slider自动播放  */
			if(options.play === true) {	
                function play(){
                    if( _ind < $wrap_li.length-1 ) {
                        _ind++;
                    } else {
                        _ind = 0;
                    };
                    $numLi.removeClass('visited');
                    $numLi.eq(_ind).addClass('visited');
					sliderMod(_ind);
					return false;
                };
                var _time = setInterval(
                    play,
                    options.play_speed);
                $wrap.hover(function(){
                    clearInterval(_time); 
                    clearInterval(xx); 
                },function(){
                    _time_2 = setInterval(
                     play,
                     options.play_speed);
                xx = _time_2
                });
			};	
		});
	};
})(jQuery)