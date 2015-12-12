$(document).ready(function(){

	mydate=new Date();
	// $("#year").val(mydate.getFullYear());
	// $("#month").val(mydate.getMonth()+1);
	// $("#day").val(mydate.getDate());
    
    $("#year").val("2015");
    $("#month").val("8");
    $("#day").val("19");
	var iTimerA; //��������
	var yy = 2011;//��
	var mm = 5;//��
	var dd = 27;//��
	var ty = 28;//�¾�����
	var d_str = '';//ʱ�����ַ���
	var week_str = '';//�������ַ���
	var bb_w_str = '';//̥�������ַ���
	var bb_l_str = '';//̥�����ַ���
	var bb_s_str = '';//̥��״̬�ַ���
	var mm_w_str = '';//�и����������ַ���
	var mm_j_str = '';//��ǰ���
	var tips_str = '';
	var tt = 280*24*3600*1000;
	var mday = 24*3600*1000;//�м��
	var hdays;
	var bb_weight = ['','','','','','','','','1��','2��','4��','7��','14��','25��','45��','70��','100��','140��','190��','240��','300��','360��','430��','501��','600��','700��','800��','900��','1001��','1175��','1350��','1501��','1675��','1825��','2001��','2160��','2340��','2501��','2775��','3001��','3250��','3501��','4001��'];//���ر�
	var bb_height = ['','','','','','','','','4����','','6.5����','','9����','','12.5����','','16����','','20.5����','','25����','','27.5����','','30����','','32.5����','','35����','','37.5����','','40����','','42.5����','','45����','','47.5����','','50����','',''];//��߱�
	var mm_weight = ['','','','','','','','','0.5ǧ��','0.7ǧ��','0.9ǧ��','1.1ǧ��','1.4ǧ��','1.7ǧ��','2.0ǧ��','2.3ǧ��','2.7ǧ��','3.0ǧ��','3.4ǧ��','3.8ǧ��','4.3ǧ��','4.7ǧ��','5.1ǧ��','5.5ǧ��','5.9ǧ��','6.4ǧ��','6.8ǧ��','7.2ǧ��','7.4ǧ��','7.7ǧ��','8.1ǧ��','8.4ǧ��','8.8ǧ��','9.1ǧ��','9.5ǧ��','10.0ǧ��','10.4ǧ��','10.5ǧ��','11.0ǧ��','11.3ǧ��','','',''];//�и��������ӱ�	
	
	//����ʱ����
	function gen_dateline(yy,mm,dd){

		d_str = '';
		week_str = '';
		bb_w_str = '';
		bb_l_str = '';
		bb_s_str = '';
		mm_w_str = '';
		mm_j_str = '';
		tips_str = '';

		var bdate = Date.UTC(yy,mm-1,dd); //ĩ���¾�ʱ��
		if(dd>=14){
			var sdate = Date.UTC(yy,mm-1,1);//��ʼ��
		}else{
			var sdate = bdate - 14*24*3600*1000;
		}
		var demodate = new Date();
		var ndate = Date.UTC(demodate.getFullYear(),demodate.getMonth(),demodate.getDate());//��ǰʱ��
		hdays = (ndate-bdate)/1000/3600/24;//��������
	    var weeks = parseInt(hdays/7); 
        var hdays2 = hdays%7;        

        var fdate = new Date(bdate+tt+(ty-28)*24*3600*1000);//Ԥ����
		if(hdays > 294 ){
			alert("�Ѿ����س���Ԥ���ڣ���ȷ������������ȷ��");
			return;
		}
		else if(hdays<0){
			alert("����δ���У���ȷ������������ȷ��");
			return;
		}

		$("#gj_info").hide();
		$("#dateline").css("width","449px").css("height","255px").css("background","url(images/line-bg.png)");
		$("#menu,#other").show();


		$("#cy").text(fdate.getFullYear());
		$("#cm").text(fdate.getMonth()+1);
		$("#cd").text(fdate.getDate());
		$("#ccd").text(hdays+"��(" + weeks + "��+"+ hdays2 +"��)");
		//alert("Ԥ���ڣ�" + fdate.getFullYear() + "��" + (fdate.getMonth()+1) + "��" + fdate.getDate() + "��");
		//var t1 = new Date(yy,mm,0).getDate();//���е���һ������
		if(dd<14)dd=14;
		var t2 = 280 + dd + 14;//���е���+42����������
		for(var i=0;i<t2;i++){
			demodate = new Date(sdate+i*mday);
			var m = demodate.getMonth()+1;
			var d = demodate.getDate();
			var y = demodate.getFullYear();
			
			//����ʱ����
			if(d==1 || i==0){
				d_str += "</dl><dl><dt>" + y + "��" + m + "��</dt>\n";
			}
			d_str += "<dd class=";
			if(d==1 || i==0 || i == dd || i == (280+dd))d_str += "d1>";
			else if (i==(t2-1))d_str += "d1 id=end>";
			else if(d%5==1)d_str += "d2>" + (d-1);
			else d_str += "d3>";
			d_str += "</dd>\n";

			//̥��״̬
			/*if(i == dd)tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db1.gif) repeat-y;'>��ĩ���¾���1��</span>";
			if((dd + 2*7)== i)tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db3.gif) repeat-y;'>��������</span>";
			if((dd + 3*7)== i)tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db3.gif) repeat-y;'>�Ŵ�</span>";
			if((dd + 4*7)== i)tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db3.gif) repeat-y;'>����ͷ������</span>";*/
			if(hdays+dd==i)$("#now").show().css('left',(i*10-7))
			switch(i-dd){
				case 0:
					tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db1.gif) repeat-y;width:140px'>��ĩ���¾���1��</span>";
					break;
				case 14:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>������</span>";
					break;
				case 21:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>�Ŵ�</span>";
					break;
				case 28:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>����ͷ������</span>";
					break;
				case 42:
					tips_str += "<span style='margin-left:" + (i*10) + "px;'>������ʼ</span>";
					mm_j_str += "<span style='margin-left:" + (i*10-70) + "px;'>��6������</span>"; //���죺6��
					break;
				case 56:
					tips_str += "<span style='margin-left:" + (i*10) + "px;'>�������</span>";
					mm_j_str += "<span style='margin-left:70px;'>���￴���</span>"; //���죺8��
					break;
				case 70:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>�������� �������</span>";
					break;
				case 84:
					tips_str += "<span style='margin-left:" + (i*10) + "px;'>�ڴ�����</span>";
					mm_j_str += "<span style='margin-left:210px;line-height:16px;padding-top:4px;'>��1��<br>��ʽ����</span>"; //���죺12��
					break;
				case 91:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;width:140px'>����ë�� ����</span>";
					break;
				case 105:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>�ɱ��Ա�</span>";
					break;
				case 112:
					mm_j_str += "<span style='margin-left:210px;'>16�ܲ���</span>"; //���죺16��
					break;
				case 119:
					mm_j_str += "<span style='width:140px;background:url();'>16-18������ɸ��</span>"; //���죺16��
					break;
				case 126:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>ָ��ë������</span>";
					break;
				case 140:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>������Ըе�̥��</span>";
					mm_j_str += "<span style='margin-left:70px;line-height:16px;padding-top:4px;'>20�ܲ���<br>̥��������</span>"; //���죺20��
					break;
				case 154:
					tips_str += "<span style='margin-left:" + (i*10) + "px;padding-top:185px;'>��ʼ����<br>��θ�䶯</span>";
					break;
				case 161:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>�ɸо�����</span>";
					break;
				case 168:
					mm_j_str += "<span style='margin-left:210px;line-height:16px;padding-top:4px;'>24�ܲ���<br>���򲡼��</span>"; //���죺24��
					break;
				case 196:
					tips_str += "<span style='margin-left:" + (i*10) + "px;width:140px'>��ʼ���� ��ˮ�����β�</span>";
					mm_j_str += "<span style='margin-left:210px;'>28�ܲ���</span>"; //���죺28��
					break;
				case 224:
					mm_j_str += "<span style='margin-left:210px;'>32�ܲ���</span>"; //���죺32��
					break;
				case 238:
					mm_j_str += "<span style='margin-left:70px;line-height:16px;padding-top:4px;'>34�ܲ���<br>������ ��Ѫ</span>"; //���죺34��
					break;
				case 245:
					tips_str += "<span style='margin-left:" + ((i*10)-6) + "px;background:url(images/tri.png) no-repeat;background-position:0 180px;padding-left:0;padding-top:195px;'>�β�����</span>";
					break;
				case 252:
					mm_j_str += "<span style='margin-left:70px;'>36�ܲ���</span>"; //���죺36��
					break;
				case 259:
					mm_j_str += "<span>37�ܲ���</span>"; //���죺37��
					break;
				case 266:
					tips_str += "<span style='margin-left:" + (i*10) + "px;'>��θ����</span>";
					mm_j_str += "<span style='line-height:16px;padding-top:4px;'>38�ܲ���<br>̥λ����</span>"; //���죺38��
					break;
				case 273:
					mm_j_str += "<span>39�ܲ���</span>"; //���죺39��
					break;
				case 280:
					tips_str += "<span style='margin-left:" + (i*10) + "px;background:url(images/db1.gif) repeat-y;'>��Ԥ����</span>";
					mm_j_str += "<span>40�ܲ���</span>"; //���죺40��
					break;
			}
			

			//�������������ء������и�����
			if(i>=dd && (i-dd)%7==0) {
				if(i==dd){
					if( (i-hdays-dd+7>=0) && (i-hdays-dd<=0)) week_str += "<span style='margin-left:" + (i*10)+ "px;'><a href='http://www.berqin.com/age/huaiyun1w/' target=_blank title='����鿴����̥����������(ͼ��)'><img src=images/i.gif>��1��</a></span>";//������
					else week_str += "<span style='margin-left:" + (i*10)+ "px;'><a href='http://www.berqin.com/age/huaiyun1w/' target=_blank title='����鿴����̥����������(ͼ��)'>��1��</a></span>";
					bb_w_str += "<span style='margin-left:" + (i*10)+ "px;'>"+ bb_weight[0] +"</span>";//����
					bb_l_str += "<span style='margin-left:" + (i*10)+ "px;'>"+ bb_height[0] +"</span>";//��
					mm_w_str += "<span style='margin-left:" + (i*10)+ "px;'>"+ bb_height[0] +"</span>";//�и���������
				}
				else {
					if((i-dd)/7>39) week_str += "<span>��" + ((i-dd)/7+1) + "��</span>";
					else if( (i-hdays-dd+7>=0) && (i-hdays-dd<=0))week_str += "<span><a href='http://www.berqin.com/age/huaiyun"+((i-dd)/7+1)+"w/' target=_blank title='����鿴����̥����������(ͼ��)'><img src=images/i.gif>��" + ((i-dd)/7+1) + "��</a></span>";
					else week_str += "<span><a href='http://www.berqin.com/age/huaiyun"+((i-dd)/7+1)+"w/' target=_blank title='����鿴����̥����������(ͼ��)'>��" + ((i-dd)/7+1) + "��</a></span>";
					bb_w_str += "<span>" + bb_weight[(i-dd)/7] + "</span>";
					if(((i-dd)/7+1)%2==1)bb_l_str += "<span>"+ bb_height[(i-dd)/7] +"</span>";
					mm_w_str += "<span>"+ mm_weight[(i-dd)/7] +"</span>";
				}
			}

			//��ǰ������
		}

		//�ػ�ʱ����
		$("#date").empty().append("<dl>"+d_str+"</dl>");

		//����״̬
		$("#tips").empty().append(tips_str);

		//�ػ�������
		$("#week").empty().append(week_str);

		//�ػ�̥��������
		$("#bb_w").empty().append(bb_w_str);

		//�ػ�����
		$("#bb_l").empty().append(bb_l_str);

		//�ػ��и�ƽ��������
		$("#mm_w").empty().append(mm_w_str);

		//�ػ��ǰ���
		$("#mm_j").empty().append(mm_j_str);

		//$("#text1").val(mm_j_str);
		var ftl = -dd*10-hdays*10+140;
		$("#con").css('left',ftl);
	}
	
	$("#btn1").click(function(){
		checkage();
		//��λʱ����	
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
		if($("#year").val()=='' || $("#month").val()=='' || $("#day").val()==''){alert("���������ڣ�");return;}
		var i_year = parseInt($("#year").val());
		var i_month = parseInt($("#month").val());
		var i_day = parseInt($("#day").val());

		if(i_month < 1 || i_month > 12){alert("�·��������");return;}
		if(i_day < 1){alert("�����������");return;}
		if(i_day > new Date(i_year,i_month,0).getDate()){alert(i_year+'��'+i_month+'��û�е�'+i_day+'�죡');return;}

		if(i_year+1< new Date().getFullYear()){alert("�����������ݣ�");return;}


		yy = parseInt($("#year").val());//��
		mm = parseInt($("#month").val());//��
		dd = parseInt($("#day").val());//��
		ty = parseInt($("#mweek").val());//�¾�����

		gen_dateline(yy,mm,dd);
	}
	//���̿��Ʒ���
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
