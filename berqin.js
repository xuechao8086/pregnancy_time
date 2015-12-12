$(document).ready(function(){

	mydate=new Date();
	// $("#year").val(mydate.getFullYear());
	// $("#month").val(mydate.getMonth()+1);
	// $("#day").val(mydate.getDate());
    
    $("#year").val("2015");
    $("#month").val("8");
    $("#day").val("19");
	var iTimerA; //滚动计数
	var yy = 2011;//年
	var mm = 5;//月
	var dd = 27;//日
	var ty = 28;//月经周期
	var d_str = '';//时间轴字符串
	var week_str = '';//妊娠周字符串
	var bb_w_str = '';//胎儿体重字符串
	var bb_l_str = '';//胎儿身长字符串
	var bb_s_str = '';//胎儿状态字符串
	var mm_w_str = '';//孕妇体重增加字符串
	var mm_j_str = '';//产前检查
	var tips_str = '';
	var tt = 280*24*3600*1000;
	var mday = 24*3600*1000;//中间差
	var hdays;
	var bb_weight = ['','','','','','','','','1克','2克','4克','7克','14克','25克','45克','70克','100克','140克','190克','240克','300克','360克','430克','501克','600克','700克','800克','900克','1001克','1175克','1350克','1501克','1675克','1825克','2001克','2160克','2340克','2501克','2775克','3001克','3250克','3501克','4001克'];//体重表
	var bb_height = ['','','','','','','','','4厘米','','6.5厘米','','9厘米','','12.5厘米','','16厘米','','20.5厘米','','25厘米','','27.5厘米','','30厘米','','32.5厘米','','35厘米','','37.5厘米','','40厘米','','42.5厘米','','45厘米','','47.5厘米','','50厘米','',''];//身高表
	var mm_weight = ['','','','','','','','','0.5千克','0.7千克','0.9千克','1.1千克','1.4千克','1.7千克','2.0千克','2.3千克','2.7千克','3.0千克','3.4千克','3.8千克','4.3千克','4.7千克','5.1千克','5.5千克','5.9千克','6.4千克','6.8千克','7.2千克','7.4千克','7.7千克','8.1千克','8.4千克','8.8千克','9.1千克','9.5千克','10.0千克','10.4千克','10.5千克','11.0千克','11.3千克','','',''];//孕妇体重增加表	
	
	//生成时间轴
	function gen_dateline(yy,mm,dd){

		d_str = '';
		week_str = '';
		bb_w_str = '';
		bb_l_str = '';
		bb_s_str = '';
		mm_w_str = '';
		mm_j_str = '';
		tips_str = '';

		var bdate = Date.UTC(yy,mm-1,dd); //末次月经时间
		if(dd>=14){
			var sdate = Date.UTC(yy,mm-1,1);//起始月
		}else{
			var sdate = bdate - 14*24*3600*1000;
		}
		var demodate = new Date();
		var ndate = Date.UTC(demodate.getFullYear(),demodate.getMonth(),demodate.getDate());//当前时间
		hdays = (ndate-bdate)/1000/3600/24;//怀孕天数
	    var weeks = parseInt(hdays/7); 
        var hdays2 = hdays%7;        

        var fdate = new Date(bdate+tt+(ty-28)*24*3600*1000);//预产期
		if(hdays > 294 ){
			alert("已经严重超出预产期！您确定输入日期正确吗？");
			return;
		}
		else if(hdays<0){
			alert("您尚未怀孕！您确定输入日期正确吗？");
			return;
		}

		$("#gj_info").hide();
		$("#dateline").css("width","449px").css("height","255px").css("background","url(images/line-bg.png)");
		$("#menu,#other").show();


		$("#cy").text(fdate.getFullYear());
		$("#cm").text(fdate.getMonth()+1);
		$("#cd").text(fdate.getDate());
		$("#ccd").text(hdays+"天(" + weeks + "周+"+ hdays2 +"天)");
		//alert("预产期：" + fdate.getFullYear() + "年" + (fdate.getMonth()+1) + "月" + fdate.getDate() + "日");
		//var t1 = new Date(yy,mm,0).getDate();//怀孕当月一共天数
		if(dd<14)dd=14;
		var t2 = 280 + dd + 14;//怀孕当月+42周满的天数
		for(var i=0;i<t2;i++){
			demodate = new Date(sdate+i*mday);
			var m = demodate.getMonth()+1;
			var d = demodate.getDate();
			var y = demodate.getFullYear();
			
			//生成时间线
			if(d==1 || i==0){
				d_str += "</dl><dl><dt>" + y + "年" + m + "月</dt>\n";
			}
			d_str += "<dd class=";
			if(d==1 || i==0 || i == dd || i == (280+dd))d_str += "d1>";
			else if (i==(t2-1))d_str += "d1 id=end>";
			else if(d%5==1)d_str += "d2>" + (d-1);
			else d_str += "d3>";
			d_str += "</dd>\n";

			//胎儿状态
			/*if(i == dd)tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db1.gif) repeat-y;'>←末次月经第1天</span>";
			if((dd + 2*7)== i)tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db3.gif) repeat-y;'>←排卵日</span>";
			if((dd + 3*7)== i)tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db3.gif) repeat-y;'>着床</span>";
			if((dd + 4*7)== i)tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db3.gif) repeat-y;'>已有头和躯干</span>";*/
			if(hdays+dd==i)$("#now").show().css('left',(i*10-7))
			switch(i-dd){
				case 0:
					tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db1.gif) repeat-y;width:140px'>←末次月经第1天</span>";
					break;
				case 14:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>排卵日</span>";
					break;
				case 21:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>着床</span>";
					break;
				case 28:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>已有头和躯干</span>";
					break;
				case 42:
					tips_str += "<span style='margin-left:" + (i*10) + "px;'>心跳开始</span>";
					mm_j_str += "<span style='margin-left:" + (i*10-70) + "px;'>第6周验孕</span>"; //产检：6周
					break;
				case 56:
					tips_str += "<span style='margin-left:" + (i*10) + "px;'>心脏成型</span>";
					mm_j_str += "<span style='margin-left:70px;'>回诊看结果</span>"; //产检：8周
					break;
				case 70:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>骨骼发育 手足成型</span>";
					break;
				case 84:
					tips_str += "<span style='margin-left:" + (i*10) + "px;'>口唇成型</span>";
					mm_j_str += "<span style='margin-left:210px;line-height:16px;padding-top:4px;'>第1次<br>正式产检</span>"; //产检：12周
					break;
				case 91:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;width:140px'>生长毛发 牙苞</span>";
					break;
				case 105:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>可辨性别</span>";
					break;
				case 112:
					mm_j_str += "<span style='margin-left:210px;'>16周产检</span>"; //产检：16周
					break;
				case 119:
					mm_j_str += "<span style='width:140px;background:url();'>16-18周唐氏筛查</span>"; //产检：16周
					break;
				case 126:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>指甲毛发长成</span>";
					break;
				case 140:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>妈妈可以感到胎动</span>";
					mm_j_str += "<span style='margin-left:70px;line-height:16px;padding-top:4px;'>20周产检<br>胎儿超声波</span>"; //产检：20周
					break;
				case 154:
					tips_str += "<span style='margin-left:" + (i*10) + "px;padding-top:185px;'>开始吞咽<br>肠胃蠕动</span>";
					break;
				case 161:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>可感觉声音</span>";
					break;
				case 168:
					mm_j_str += "<span style='margin-left:210px;line-height:16px;padding-top:4px;'>24周产检<br>糖尿病检查</span>"; //产检：24周
					break;
				case 196:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>开始呼吸 羊水进出肺部</span>";
					mm_j_str += "<span style='margin-left:210px;'>28周产检</span>"; //产检：28周
					break;
				case 224:
					mm_j_str += "<span style='margin-left:210px;'>32周产检</span>"; //产检：32周
					break;
				case 238:
					mm_j_str += "<span style='margin-left:70px;line-height:16px;padding-top:4px;'>34周产检<br>超声波 验血</span>"; //产检：34周
					break;
				case 245:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>肺部成熟</span>";
					break;
				case 252:
					mm_j_str += "<span style='margin-left:70px;'>36周产检</span>"; //产检：36周
					break;
				case 259:
					mm_j_str += "<span>37周产检</span>"; //产检：37周
					break;
				case 266:
					tips_str += "<span style='margin-left:" + (i*10) + "px;'>肠胃成熟</span>";
					mm_j_str += "<span style='line-height:16px;padding-top:4px;'>38周产检<br>胎位评估</span>"; //产检：38周
					break;
				case 273:
					mm_j_str += "<span>39周产检</span>"; //产检：39周
					break;
				case 280:
					tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db1.gif) repeat-y;'>←预产期</span>";
					mm_j_str += "<span>40周产检</span>"; //产检：40周
					break;
			}
			

			//妊娠周数、体重、身长、孕妇体重
			if(i>=dd && (i-dd)%7==0) {
				if(i==dd){
					if( (i-hdays-dd+7>=0) && (i-hdays-dd<=0)) week_str += "<span style='margin-left:" + (i*10)+ "px;'><a href='http://www.berqin.com/age/huaiyun1w/' target=_blank title='点击查看本周胎儿发育详情(图解)'><img src=images/i.gif>第1周</a></span>";//妊娠周
					else week_str += "<span style='margin-left:" + (i*10)+ "px;'><a href='http://www.berqin.com/age/huaiyun1w/' target=_blank title='点击查看本周胎儿发育详情(图解)'>第1周</a></span>";
					bb_w_str += "<span style='margin-left:" + (i*10)+ "px;'>"+ bb_weight[0] +"</span>";//体重
					bb_l_str += "<span style='margin-left:" + (i*10)+ "px;'>"+ bb_height[0] +"</span>";//身长
					mm_w_str += "<span style='margin-left:" + (i*10)+ "px;'>"+ bb_height[0] +"</span>";//孕妇体重增加
				}
				else {
					if((i-dd)/7>39) week_str += "<span>第" + ((i-dd)/7+1) + "周</span>";
					else if( (i-hdays-dd+7>=0) && (i-hdays-dd<=0))week_str += "<span><a href='http://www.berqin.com/age/huaiyun"+((i-dd)/7+1)+"w/' target=_blank title='点击查看本周胎儿发育详情(图解)'><img src=images/i.gif>第" + ((i-dd)/7+1) + "周</a></span>";
					else week_str += "<span><a href='http://www.berqin.com/age/huaiyun"+((i-dd)/7+1)+"w/' target=_blank title='点击查看本周胎儿发育详情(图解)'>第" + ((i-dd)/7+1) + "周</a></span>";
					bb_w_str += "<span>" + bb_weight[(i-dd)/7] + "</span>";
					if(((i-dd)/7+1)%2==1)bb_l_str += "<span>"+ bb_height[(i-dd)/7] +"</span>";
					mm_w_str += "<span>"+ mm_weight[(i-dd)/7] +"</span>";
				}
			}

			//产前检查进度
		}

		//重绘时间线
		$("#date").empty().append("<dl>"+d_str+"</dl>");

		//宝宝状态
		$("#tips").empty().append(tips_str);

		//重绘妊娠线
		$("#week").empty().append(week_str);

		//重绘胎儿体重线
		$("#bb_w").empty().append(bb_w_str);

		//重绘身长线
		$("#bb_l").empty().append(bb_l_str);

		//重绘孕妇平均体重增
		$("#mm_w").empty().append(mm_w_str);

		//重绘产前检查
		$("#mm_j").empty().append(mm_j_str);

		//$("#text1").val(mm_j_str);
		var ftl = -dd*10-hdays*10+140;
		$("#con").css('left',ftl);
	}
	
	$("#btn1").click(function(){
		checkage();
		//复位时间线	
	});


	function a(){  
		 var lf = parseInt($("#con").css('left'));
		 var nl = $("#end").offset().left - $("#dateline").offset().left;
		if(nl-10>=420)$("#con").css("left",(lf-5)+"px").css("left",(lf-10)+"px"); 
	}  
	function b(){  
		 var lf = parseInt($("#con").css('left'));
		 if(lf+10<=-5)$("#con").css("left",(lf+5)+"px").css("left",(lf+10)+"px"); 
	} 
	$("#tr").mousedown(function(){
		$(this).css("padding","1px 0 0 1px");
		iTimerA = setInterval(a,50); 
	});
	$("#tr").mouseup(function(){
		$(this).css("padding","0");
		clearInterval(iTimerA); 
	});
	$("#tf").mousedown(function(){
		$(this).css("padding","1px 0 0 1px");
		iTimerA = setInterval(b,50);
	});
	$("#tf").mouseup(function(){
		$(this).css("padding","0");
		clearInterval(iTimerA);
	});

	$("body").mouseup(function(){
		$("#tr,#tf").css("padding","0");
		clearInterval(iTimerA);
	});

	function checkage(){
		if($("#year").val()=='' || $("#month").val()=='' || $("#day").val()==''){alert("请输入日期！");return;}
		var i_year = parseInt($("#year").val());
		var i_month = parseInt($("#month").val());
		var i_day = parseInt($("#day").val());

		if(i_month < 1 || i_month > 12){alert("月份输入错误！");return;}
		if(i_day < 1){alert("日期输入错误！");return;}
		if(i_day > new Date(i_year,i_month,0).getDate()){alert(i_year+'年'+i_month+'月没有第'+i_day+'天！');return;}

		if(i_year+1< new Date().getFullYear()){alert("请输入合理年份！");return;}


		yy = parseInt($("#year").val());//年
		mm = parseInt($("#month").val());//月
		dd = parseInt($("#day").val());//日
		ty = parseInt($("#mweek").val());//月经周期

		gen_dateline(yy,mm,dd);
	}
	//键盘控制方向
	$(document).keydown(function(e) {
		if(e.which == 37){
			var lf = parseInt($("#con").css('left'));
			if(lf+10<=-5)$("#con").css("left",(lf+5)+"px").css("left",(lf+10)+"px");
		}
		if(e.which == 39){
			var lf = parseInt($("#con").css('left'));
			var nl = $("#end").offset().left - $("#dateline").offset().left;
			if(nl-10>=420)$("#con").css("left",(lf-5)+"px").css("left",(lf-10)+"px"); 
		}
		if(e.which == 13){
			checkage();
		}
	});

    checkage();    

});
