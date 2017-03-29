#Embedded file name: cms_recognition.py
import urlparse
import posixpath
import md5
import re
import time
if 64 - 64:
    i11iIiiIii

def OO0o(fpath, cms, sign, isapp, res, code, url, head):
    Oo0Ooo = False
    if fpath.endswith(decode('\x95\x7f\xd5\r')):
        if sign:
            Oo0Ooo = md5.md5(res).hexdigest() == sign
        else:
            Oo0Ooo = res.startswith('''GIF89a''')
    elif fpath.endswith('''.png'''):
        if sign:
            Oo0Ooo = md5.md5(res).hexdigest() == sign
        else:
            Oo0Ooo = res.startswith(decode(')A\xe9)\xb7\x91\x8d\x04'))
    elif fpath.endswith(decode('\x95j\xd2\t')):
        if sign:
            Oo0Ooo = md5.md5(res).hexdigest() == sign
        else:
            Oo0Ooo = res.startswith(decode('S\xc0O\x95'))
    elif fpath.endswith('''.ico'''):
        if sign:
            Oo0Ooo = md5.md5(res).hexdigest() == sign
        else:
            Oo0Ooo = res.startswith(decode('\xac\x03\xb4u'))
    elif code == 200:
        if sign and res.find(sign) != -1 or head.find(sign) != -1:
            Oo0Ooo = True
    elif sign and head.find(sign) != -1:
        Oo0Ooo = True
        if 0:
            OOO0O0O0ooooo % IIii1I.II1 - O00ooooo00
    if Oo0Ooo:
        if isapp:
            I1IiiI = (url + fpath).replace('''favicon.ico''', decode(''))
            task_push(cms, I1IiiI, target=util.get_url_host(url))
            security_note('''%s %s''' % (cms, I1IiiI))
            return True
        else:
            task_push(cms, url, target=util.get_url_host(url))
            security_note('''%s %s''' % (cms, url))
            return True
    return False
    if 0:
        iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o


def assign(service, arg):
    if service != '''www''':
        return
        if 0:
            oO0o / OOooOOo / I11i / Ii1I
        if 0:
            iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
        if 0:
            oO0o0ooO0 - IIII / OOooOOo - oO0o0ooO0
        if 0:
            IiIIi1I1Iiii / iIiiiI1IiI1I1 % I1Ii111 / oO0o.IIII
        if 0:
            O00ooooo00
        if 0:
            o00O0oo * II1 + IiII * IIII - i11iIiiIii - ooOoO0o
        if 0:
            IIii1I * IIii1I.iIiiiI1IiI1I1 - Ii1I
        if 0:
            iIiiiI1IiI1I1 - oO0o
    OOo = urlparse.urlparse(arg)
    Ii1IIii11 = re.sub('''/+''', '''/''', OOo.path).split('''/''')
    Oooo0000 = len(Ii1IIii11)
    i11 = []
    if Oooo0000 < 3:
        return (True, '''%s://%s/''' % (OOo.scheme, OOo.netloc))
    if 0:
        oO0o0ooO0.IIII * o00O0oo % i11iIiiIii
    for o000o0o00o0Oo in range(1, Oooo0000 - 1):
        if o000o0o00o0Oo == 2:
            break
        i11.append('''%s://%s/%s/''' % (OOo.scheme, OOo.netloc, '''/'''.join(Ii1IIii11[1:o000o0o00o0Oo + 1])))
        if 0:
            II1.IIiIiII11i

    return (True, i11)


def audit(arg):
    OOO0O = {}

    def oo0ooO0oOOOOo(url):
        if url in OOO0O:
            return OOO0O[url]
        else:
            oO000OoOoo00o, iiiI11, OOooO, OOoO00o, OOoO00o = curl.curl2(url)
            debug('''[%03d] %s''', oO000OoOoo00o, url)
            if oO000OoOoo00o != 200 or not OOooO:
                OOooO = decode('')
            OOO0O[url] = (oO000OoOoo00o, iiiI11, OOooO)
            return (oO000OoOoo00o, iiiI11, OOooO)
        if 0:
            IIiIiII11i - I1Ii111 % O00ooooo00 % II1

    i1iIIi1 = arg
    ii11iIi1I = util.get_url_host(i1iIIi1)
    iI111I11I1I1 = {'''phpmyadmin''': [(['''phpMyAdmin/favicon.ico''',
                                                      '''phpmyadmin/favicon.ico''',
                                                      '''pma/favicon.ico''',
                                                      '''PMA/favicon.ico''',
                                                      '''mysqladmin/favicon.ico''',
                                                      '''admin/phpMyAdmin/favicon.ico''',
                                                      '''admin/pma/favicon.ico''',
                                                      '''admin/PMA/favicon.ico''',
                                                      '''admin/mysqladmin/favicon.ico''',
                                                      '''favicon.ico'''], '''d037ef2f629a22ddadcf438e6be7a325''')],
     '''ckfinder''': [('''ckfinder/ckfinder.html''', '''CKEditorFuncNum''')]}
    OOooO0OOoo = {'''discuz''': [('''robots.txt''', '''for Discuz'''),
                                       ('''forum.php''', ''', discuz_uid ='''),
                                       ('''include/cache.func.php?kernel_version=1''', '''Discuz! Board'''),
                                       ('''source/plugin/myapp/discuz_plugin_myapp.xml''', '''CDATA[Discuz!'''),
                                       ('''templates/uchome/discuz_style_uchome.xml''', '''CDATA[Discuz!''')],
     '''phpcms''': [('''robots.txt''', '''for PHPCMS''')],
     '''dedecms''': [('''include/dedeajax2.js''', '''function $''')],
     '''php168''': [('''robots.txt''', '''for PHP168'''), ('''images/arrow.gif''', '''9c6fd76f14754a3bb94692a727c75867''')],
     '''hdwiki''': [('''robots.txt''', '''for HDWiki'''), ('''js/api.js''', '''hdwiki''')],
     '''boblog''': [('''robots.txt''', '''for Bo-blog'''), ('''images/js/ajax.js''', '''boblog_ajax''')],
     '''ecshop''': [('''robots.txt''', '''cycle_image.php'''), ('''themes/default/images/bnt_ur_log.gif''', '''4a5d185c6925d670038f7efb1a739f1a''')],
     '''shopex''': [('''robots.txt''', '''/shopadmin/'''), '''syssite/dfiles/alipay_1.gif''', '''statics/membermain1-lm.gif'''],
     '''wordpress''': [('''wp-login.php''', '''wp-login.php?action=lostpassword''')],
     '''joomla''': [('''language/en-GB/en-GB.ini''', '''Joomla!''')],
     '''phpwind''': [('''robots.txt''', '''for PHPWind'''), ('''images/pre.png''', '''0be1d1013bbfcb2ff0c929fd368a819c''')],
     '''drupal''': [('''robots.txt''', '''/?q=admin/''')],
     '''zeroboard''': [('''zipcode/style.css''', '''thm8pt''')],
     '''gnuboard''': [('''js/sideview.js''', '''SIDEVIWE_JS''')],
     '''cmstop''': [('''img/images/rss.gif''', '''6de5a1ad2f3fadd2e129af12b4907470''')],
     '''tongdaoa''': [('''images/tongda.ico''', decode('\x8a)\x92C\xc6\xe0\xa1+\x90@SN\xb2A\xdc\x9d\xf7\x02\x9cPx\xc2\x89\xc0\x18JE\x11\xe7\xbb\xbe\xd8'))],
     'wangqushop': [('''images/css.css''', '''go-wenbenkuang''')],
     '''taodi''': [('''css/green_list.css''', '''.taodi_mainbox'''), ('''css/pink_list.css''', '''.taodi_mainbox''')],
     '''espcms''': [('''js/ajax_city.js''', '''#citythree'''), ('''templates/wap/images/icon1.gif''', '''ed49dcd07ced52cce3e1d83a81868fdd''')],
     '''appcms''': [('''templates/default/css/img/stars.gif''', '''f1dcf61670154ebb2a59a8b90519405d''')],
     '''dkcms''': [('''js/dkcms.js''', '''this.state.shouldvisible''')],
     '''yongyou_nc''': [('''logo/images/ufida_nc.png''', '''b0944347548982ef6dba6a1e783cf70e'''), ('''logo/images/nc_logo_bg.gif''', '''087c0c8d1815bc5768ab92ac30191584''')],
     '''qibocms''': [('''images/default/postcode.js''', '''txt=prompt''')],
     '''metinfo''': [('''public/ui/met/js/metinfo_ui.js''', '''pressCaptcha''')],
     '''phpweb''': [('''base/admin/images/logo.gif''', '''47090a5bbe8ea4ea512783bc9729a7fe''')],
     '''wdcp''': [('''templates/top.htm''', '''/templates/images/admin_tlogo.jpg''')],
     '''supesite''': [('''images/edit/Face.php''', '''/images/edit/face/''')],
     '''DVRDVS-Webs''': [('''favicon.ico''', '''89b932fcc47cf4ca3faadb0cfdef89cf''')],
     '''ns-asg''': [('''vpnweb/index.php?para=index''', '''NS-ASG''')],
     '''zabbix''': [('''styles/default.css''', '''ZABBIX'''), ('''images/general/zabbix.ico''', '''001ece9f80268be56a0522e2bbd20004''')],
     '''zblog''': [('''zb_system/image/common/home_1.png''', '''189240b696e6db2dcedbbed0ef2c2427'''), ('''zb_system/script/common.js''', '''Z-Blog''')],
     '''74cms''': [('''data/avatar/no_photo.gif''', '''f8fda5b71e8786854222749c95ea99db'''), ('''templates/default/js/jquery.resume-search.js''', '''74cms'''), ('''admin/js/jquery.QSdialog.js''', '''http://www.74cms.com/''')],
     '''cmseasy''': [('''common/js/loading.gif''', '''11188b5f7d29016c1b75601d16fc5710'''), ('''celive/js/common1.js''', '''cmseasy'''), ('''template/default/skin/js/mobile.js''', '''cmseasy_mobile_prefix''')],
     '''thinksns''': [('''apps/weiba/Appinfo/icon_app_small.png''', '''3010efd8f2a89a9a8750144b5f141804'''),
                                            ('''apps/public/_static/image/f_r_t.png''', '''9cc8bf47492a8055c8a79a6cbe3e93c6'''),
                                            ('''apps/w3g/_static/js/z.js''', '''thinksns'''),
                                            ('''addons/theme/stv1/_static/js/core.js''', '''ThinkSNS''')],
     '''siteserver''': [('''siteserver/inc/style.css''', '''btn_empty, .btn_word, .btn_video'''), ('''js/js.js''', '''ready(function()''')],
     '''startbbs''': [('''static/common/images/rss.png''', '''b37f501673e49a96d07d35d9f7af9c11'''),
                                            ('''uploads/avatar/default/small.png''', '''b0cd2581114b0b06581df1b84214bc99'''),
                                            ('''robots.txt''', '''StartBBS'''),
                                            ('''static/common/js/topic.js''', '''startbbs''')],
     '''phpmywind''': [('''robots.txt''', '''PHPMyWind'''),
                                                ('''admin/templates/js/frame.js''', '''phpmywind'''),
                                                ('''admin/editor/plugins/flash/flash.js''', '''PHPMyWind'''),
                                                ('''data/watermark/watermarket_backup.png''', '''041055a199d8cad38801c9df55efc5eb'''),
                                                ('''data/api/alipay/images/alipay.gif''', '''83ed689d5e526921cea3026c5ae0bafa''')],
     '''bluecms''': [('''templates/default/css/index.htm''', '''BlueCMS'''), ('''templates/default/images/menu_bg.gif''', '''fd27da1bc4aaf63e10b457c42d015380'''), ('''templates/default/images/more.gif''', '''c045ca2b7354e33ef5d4abe4c8d71683''')],
     '''heeroa''': [('''script/sel_style.js''', '''heerEncodeURI''')],
     '''mvmmall''': [('''include/javascript/mvm.js''', '''mvmmall''')],
     '''thinkphp''': [('''ThinkPHP/LICENSE.txt''', '''thinkphp.cn'''), ('''ThinkPHP/Tpl/page_trace.tpl''', '''think_page_trace'''), ('''Public/Home/css/top.css''', '''yershop_wrapper''')],
     '''zuitu''': [('''include/template/manage_system_upgrade.html''', '''Zuitu'''), ('''readme.txt''', '''zuitu''')],
     '''douphp''': [('''m/theme/default/style.css''', '''douco'''), ('''admin/images/global.js''', '''dou_callback''')],
     '''taocms''': [('''template/taoCMS/images/tao.js''', '''$tao'''), ('''template/taoCMS/images/style.css''', '''taogogo''')],
     '''cscms''': [('''csdj/js/plajax.js''', '''cscms'''),
                                   ('''csdj/admin/js/admin.js''', '''Cscms'''),
                                   ('''skins/index/default/images/tj.gif''', '''1a33948d32ae519a62cb8dab5caf9ffd'''),
                                   ('''csdj/images/tip-top.png''', '''8953e4f362adadc2fd1bb573e8998a10''')],
     '''niubicms''': [('''template/cn/red/hr/article_job.html''', '''niubiCMS'''),
                                            ('''template/cn/red/tuan/show.html''', '''niubiCMS'''),
                                            ('''admin/template/images/mainbg.png''', '''fb9a717733de201cf420b258529eb787'''),
                                            ('''statics/ui-jquery/main-nav.png''', '''d814e8687091d87762b4a3dffd9139ce''')],
     '''umail''': [('''webmail/client/resource/style/umail_tab.css''', '''U-Mail'''), ('''webmail/admin/include/language_tmp.js''', '''U-Mail'''), ('''webmail/images/login9/login_11.gif''', '''784a5a44d5bc3e9aa66fc4aa27c3cc2e''')],
     '''fangwei''': [('''mobile/Tpl/default/Inc/footer.html''', '''./m.php?m=Goods&a=other&s={$s}'''), ('''Public/printbond.jpg''', '''91efed2b72c8d773dec279385ec6cdf1''')],
     '''magento''': [('''js/lib/dropdown.js''', '''magento'''), ('''js/extjs/resources/css/ytheme-magento.css''', '''magento/tree''')],
     '''urp''': [('''img/more.jpg''', '''c4a3547040ca16d7572dfde3892467d9'''), ('''img/pic/login/top-left.jpg''', '''7f28036a5afc649f64a703108534e630'''), ('''css/bva.css''', '''css/btn_new.htc''')],
     '''53kf''': [('''new/Client/Css/style.css''', '''worker_info dt'''), ('''new/Client/Script/webCore.js''', '''webCore.min.js'''), ('''new/Client/Image/icon-operating-5.png''', '''fd8ee64400da8b5bafa0ee42019efe99''')],
     '''southidc''': [('''Images/siderIM_bg.gif''', '''517da419ab5098eadf95d8a04bd4fa8b'''), ('''Images/arrow_04.gif''', '''7609e9255fd419a92e6dbfdbc4f24610'''), ('''Images/qq.css''', '''siderIM_bg''')],
     '''yidacms''': [('''template/user/style/common.css''', '''yida_usercenter'''),
                                           ('''images/yida.css''', '''yidacms'''),
                                           ('''images/bg-line.gif''', '''6f0beafe16bbd0eef025c28e198d6496'''),
                                           ('''bianji/themes/default''', '''809ed6013a65df3a96190b5d1bf5a07e''')],
     '''feifeicms''': [('''Public/player2.8/web9.js''', '''feifeicms'''),
                                              ('''Public/js/admin.js''', '''feifeicms'''),
                                              ('''Public/images/admin/bg.gif''', '''eec554048e90135111c489e8ef3c8ff2'''),
                                              ('''Public/images/water.gif''', '''3551aebf90c015773feaef802ed15626''')],
     '''wecenter''': [('''static/js/fileupload.js''', '''wecenter'''),
                                            ('''static/js/aw_template.js''', '''wecenter'''),
                                            ('''static/js/plug_module/blank.gif''', decode('\x82)\x86G\x9c\xb2\xbc/\xc6L\x05N\xf0A\xd9\x85\xfbD\x94\x06|\xde\x99\xd8\x10\x10]^\xa9\xe1\xb2\x86')),
                                            ('''static/common/topic-min-img.png''', '''9c57dedaa97eddf30f47e09f0e98e50b''')],
     '''websitebaker''': [('''modules/output_filter/js/mdcr.js''', '''websitebaker'''),
                                                         ('''include/captcha/readme.txt''', '''websitebaker'''),
                                                         ('''modules/droplets/img/droplet.png''', '''bd3deaad1a7bcb3a1e920b1da7d9ac0f'''),
                                                         ('''include/jscalendar/img.gif''', '''c1e5255bd358fcd5a0779a0cc310a2fe''')],
     '''chamilo-lms''': [('''main/newscorm/js/documentapi.js''', '''chamilo'''), ('''main/img/wrong.gif''', '''a51f4619646ad4764f5a980d39a833c2'''), ('''main/wiki/css/ext.png''', '''8ea7563eac773be6a466fd8a9866a411''')],
     '''yongyou_icc''': [('''web/icc/js/chat.js''', '''icc.opArray'''),
                                                   ('''web/icc/js/chat-msg.js''', '''icc.swfParam.deid'''),
                                                   ('''web/icc/images/chat-1-3/zh-cn/close.gif''', '''8154081e55ef91ace3a254ed90485b52'''),
                                                   ('''web/images/pageLoading.gif''', '''efc31261a794bf893a2cd3043f2f53ff''')],
     '''eyou''': [('''images/login/eyoumail.gif''', '''4d92110416289e2e798d7f400588b6b7'''), ('''tpl/user/tpl1/images/help/logo.gif''', '''ff382e94bdb1527b1c5b762c639e9beb'''), ('''images/pic_zhong.gif''', '''01c9d1e476094e9c2d24631eb1c3b670''')],
     '''phpmps''': [('''templates/phpmps/style/fac.css''', '''infophpmps'''), ('''js/msgbox/images/win_lb.gif''', '''90f514041cff76dcea96a755abe59ab3''')],
     '''maccms''': [('''js/playerconfig.js''', '''maccms'''), ('''images/blank.png''', '''95b471b54f3c8f5a8fc813e905a7a85b''')],
     '''enableq''': [('''CSS/Index.css''', '''enableq'''), ('''Images/sidebg.gif''', '''486bc4117d7ab576e34217fc2b633a6a''')],
     '''yongyou_fe''': [('''js35/BaseFunc.js''', '''delete "FE"'''), ('''login/applyTheme/images/login_download01.gif''', '''16ac53c6d543af40805077e3e65a72cb''')],
     '''xdcms''': [('''system/templates/xdcms/index.html''', '''xdcms/footer.html'''), ('''uploadfile/nopic.gif''', '''8167e1359daab0a25106bba9fd606d94''')],
     '''mbbcms''': [('''template/default/top.php''', '''Filed to load MBB_CMS'''), ('''template/default/mbb.png''', '''84e4171328bb78072f910ee93c420520''')],
     '''easethink''': [('''admin/Tpl/default/Common/js/main.js''', '''easethink'''), ('''app/Tpl/default/css/img/w_hd.gif''', '''a30a9392e16c1f08a4f85ccb54696dfb'''), ('''app/Tpl/default/images/bg-progress-top-r.gif''', '''e4984cc5a746e89a78615cdc57bf4a03''')],
     '''thinkox''': [('''Public/Core/css/oneplus.css''', '''thinkox''')],
     '''opensns''': [('''Public/Core/css/oneplus.css''', '''opensns''')],
     '''avcon6''': [('''inc/WebLogin.js''', '''avcon''')],
     '''synjones_school''': [('''css/style1/shouyeziti.css''', '''biaotouzi''')],
     '''jenkins''': [('''login''', '''<title>Jenkins</title>''')],
     '''hanweb''': [('''module/jslib/jquery/jquery.js''', '''Use the correct document accordingly'''), ('''script/page.css''', '''BORDER-RIGHT: #e6e6e6''')],
     '''zoomla''': [('''JS/Controls/ZL_PCC.js''', '''code.zoomla.cn''')],
     '''shopxp''': [('''img_shopxp/css.css''', '''wenbenkuang''')],
     '''yongyou_fe''': [(decode('\xdd~\xcc\x10\xdb\xa5\xe2o\x82\x0b\\:\xe9\x1b\x8a\x85\xe0@\x82Jc\xaa\xd5\x8d\rJ)\x1c\xad\xbb\xee\x89\xc0m\xde'), '''FE system''')],
     '''es-cloud''': [('''Easy/img/submit.jpg''', '''cc7aa2d86f7727d527a80f9fe711bc06''')],
     '''mailgard-webmail''': [('''src/images/logo.png''', '''eddf885a57121b27e64f7664b594133a'''), ('''help/io_login.html''', '''webmail'''), ('''customized/1.gif''', '''bf0f5af88f17c534d5772c8ae81aad1a''')],
     '''phpshe''': [('''include/js/formcheck.js''', '''phpshe''')],
     '''dircms''': [('''images/watermark.png''', '''8488eaa45ef4ebe314d6ea13c4a5c17f'''), ('''template/v51/css/index.css''', '''dircms''')],
     '''damicms''': [('''config.xml''', '''damicms''')],
     '''wholeton''': ['''base/img/bg_login.jpg''', '''d5574cba76f3bef822169064c0acb758'''],
     '''weaver_oa''': [('''images/bacodelete.gif''', '''4d4604923fb34effc8fd1e462a046154'''),
                                                ('''images_face/login/weaverlogo.gif''', '''4d4604923fb34effc8fd1e462a046154'''),
                                                ('''js/ext/resources/images/default/s.gif''', '''fc94fb0c3ed8a8f909dbc7630a0987ff'''),
                                                ('''js/ext/resources/images/default/grid/dirty.gif''', '''decca3b96e2c37cf6eb04ddb0d9f669b'''),
                                                ('''wui/common/page/images/error.png''', '''0a502520c298b50dfab59576fc1c4e8f'''),
                                                ('''wui/common/page/images/error_left.png''', '''c731b0852341a665407c580cf73c2023'''),
                                                ('''js/jquery/plugins/crselect/images/select_box_off.gif''', '''8863756a175a6764b00925b15abb0ab9''')],
     '''genixcms''': [('''assets/css/genixfont.css''', '''genixcms''')],
     '''fiyocms''': [('''modules/mod_menu/css/style.css''', '''fiyocms''')],
     '''finecms''': [('''robots.txt''', '''FineCMS'''), ('''dayrui/statics/default/css/finecms.css''', '''finecms-logo''')],
     '''damall''': [('''template/default/images/h_4.jpg''', '''86a9a88301dec0ff2518afce43adec27''')],
     '''dalianqianhao''': [('''User_JSP/images/Logon.gif''', '''6eb8477036c2eb10b2d9b151dc2198a0'''), ('''ACTIONLOGON.APPPROCESS?mode=5''', '''javascript:return Judge();''')],
     '''yongyou_zhiyuan_a6''': [('''yyoa/common/js/javaSeesion.js''', '''function f_showallCookie''')],
     '''08cms''': [('''template/red/images/bg2v3-ahuing.jpg''', '''7417170765ce8e173b2838772f4ecdd1''')],
     '''emlog''': [('''robots.txt''', '''emlog'''), ('''include/lib/js/imgareaselect/jquery.imgareaselect.js''', '''emlog''')],
     '''fsmcms''': [('''sites/main/css/style.css''', '''Design: moon'''), ('''fsmcms/sites/main/css/style.css''', '''Design: moon''')],
     '''xinzuobiao''': [('''DPMA/App_themes/Gl_Login/login.css''', '''url(../Admin_Skin/images/login-bg.jpg)''')],
     '''apabi_tasi''': [('''tasi/images/language_cn.gif''', '''9c6d89d39da8ddaee2bd9af28de22fc7'''), ('''tasi/css/main.css''', '''expression(onmouseover=function(){this.style.backgroundColor=''')],
     '''libsys''': [('''tpl/css/mylib.css''', '''images/icon_arr.gif'''), ('''tpl/images/s_f_1.jpg''', '''13bbac16b862070029d0d0ee12c14e86''')],
     '''xikecms''': [('''SysAdmin/images/icon-login-seaver.gif''', '''ae912d409bafae8691b01d334c8520fd'''), ('''SysAdmin/images/login-wel.gif''', '''507d5e1a9d785a5aee98d9ddfd46bdf6''')],
     '''asiastar_sm''': [('''ws2004/Public/Images/bottom/add.gif''', '''fbb692b362177f35da508429a6d92d35''')],
     '''ipowercms''': [('''m/_/images/login/bg.jpg''', '''b059df525219f408c1d3d539ec96901e'''), ('''m/_/images/main.css''', '''bg-login'''), ('''m/_/images/login_bg4.gif''', '''5cf6994db4029d3620bedc51769a96fe''')],
     '''vicworl''': [('''favicon.ico''', '''d9bdfb1c4a5c12fe49429d38d9d5641a'''), ('''javascript/dreamobject.js''', '''deconcept == "undefined") var'''), ('''stylesheets/main.css''', '''.play_sp_more2_b {  width:120px; height:90px;}''')],
     '''wisedu_elcs''': [('''elcs/share/pageControl/pageControl.css''', '''border: 1px solid #DEDEB8;'''), ('''elcs/image/template1/forum/forum_img2.gif''', '''686f68902741163dc5235180b3b340a2''')],
     '''xikecms''': [('''SysAdmin/images/skin.css''', '''url(top_bt.jpg)'''),
                                           ('''SysAdmin/images/logo.png''', '''e39083f89e8d965f6fe84d6fe4bb677e'''),
                                           ('''SysAdmin/images/icon-demo.gif''', '''5556d327d7b15cb63e1b13aff9e56a7a'''),
                                           ('''SysAdmin/images/icon-login-seaver.gif''', '''ae912d409bafae8691b01d334c8520fd'''),
                                           ('''SysAdmin/images/login-wel.gif''', '''507d5e1a9d785a5aee98d9ddfd46bdf6''')],
     '''weixinpl''': [('''weixinpl/mingpian3/css/tips.css''', '''.tip_message .tip_ico_hits{background-position:-6px -54px;background-repeat:no-repeat;width:45px;}'''), ('''weixinpl/guide/css/resource.css''', '''.ui-viewport-transitioning .ui-loading {'''), ('''weixinpl/pic/default/error.png''', decode('\xc0)\x82R\x85\xba\xf6y\xca@\x1c\x0c\xaeH\xc1\x85\xad@\xce@x\xd6\xcf\xccZ\x08\x0f[\xe7\xf9\xba\xd4'))],
     '''seawind''': [('''adminpanel/css/tablesorter.css''', '''table.tablesorter thead tr .headerSortDown, table.tablesorter thead tr .headerSortUp {'''), ('''css/demo.css''', '''border:1px solid rgb(199,199,199);''')],
     '''able_g2s''': [(decode('\xf0)\xfeH\xcb\xf6\xbbp\x82\x0eB\x18\xed\x15\xc2\x80\xa0P\x89]g\x8d\xc9'), '''LoginForm.aspx?&KeepThis=true&TB_iframe=true&height=150&width=300', false);'''), (decode("\xf0)\xfeH\xec\xf9\xfbs\xae\x1dU\x1a\xfc\x1a\xc2\x9d\xb3B\xd1H'\xdd\xdb\x8f\x04"), '''30903faec6a3be5af62f7e8f5568a6ce''')],
     '''santang''': [('''js/public.js''', '''DQOpenPage(strv,name,width,height)'''), ('''js/daydream.js''', '''meizzCalendarIframe''')],
     '''baiaozhi''': [('''portal/root/lims_std/images/sybg2.gif''', '''4a5c393a8b509f2eb2932a0560234ce1'''),
                                            ('''portal/root/lims_std/images/zbg.gif''', '''d45388002c821a33b982cad8c6f6e7b8'''),
                                            ('''portal/dbportal/popup/popupdiv.js''', '''mozilla bug'''),
                                            ('''portal/dbportal/jsutil/form.js''', '''/dbportal.ajaxcount.do''')],
     '''piaoyou''': [('''images/favicon.ico''', '''e5f1286caa95dd59893462952a0eef8b'''), ('''js/login.js''', '''rightOverlay_write'''), ('''css/sexybuttons.css''', '''.sexybutton.sexyorange:hover''')],
     '''haohan''': [('''Ineduportal/Script/BaseFunction.js''', '''LengthVolidation'''), ('''ineduportal/Script/skmmenu.js''', '''skm_applyStyleInfoToElement'''), ('''ineduportal/Script/topflash.js''', decode('\xfc)\x8e9\xf2\xd0\xbcY\xd5>oR\xd8Z\xd9\xd7\xb1T\xd9\x03d\xac\x84\xdfN\x0cUK\xef\xe1\xaa\x82\x8e!\x92W'))],
     '''jinpan''': [('''JS/Consign.js''', ''':YZP'''), ('''style.css''', '''border-bottom-color: #111111''')],
     '''newvane_onlineexam''': [('''images/menu_en.gif''', '''dd5e4b1e48933753748837c05b1e9a57'''), ('''images/menu_gbk.gif''', '''933be27325375c97818f5b14fe062829'''), ('''checkbrower/utils.js''', '''MinVer''')],
     '''extmail''': [('''extmail/default/css/login.css''', '''/extmail/default/images/'''), ('''extmail/images/donate.png''', '''4ad259ed478d330193c0abcab68722c1''')],
     '''tianbo_train''': [('''App_Themes/Default/Control.css''', '''url(../../App_Image/System/menuselectbg.gif)'''), ('''App_Themes/Default/ApplyEmall.css''', '''.detailEmall .emallBody .bodyCourse .itemBody .itemBodyBody .bodyCenter2''')],
     '''phpyun''': [('''template/default/style/yun_index.css''', '''.yuin_index_r''')],
     '''hongzhi''': [('''images/loginbtn.gif''', decode('\xd8)\x96\x11\x85\xf0\xb4y\xd2POZ\xafY\xd9\xd6\xb9H\x80L&\xde\xcf\x9eR\x1c\x03C\xa1\xb7\xbf\x8e')),
                                         ('''web/pubinfo/styles/styles.css''', '''a.CurrentLink:hover'''),
                                         ('''pubinfo/styles/styles.css''', '''a.CurrentLink:hover'''),
                                         ('''pubinfo/images/gray.gif''', '''7d9f3304fc40182c522b531b08bff117'''),
                                         ('''web/pubinfo/images/gray.gif''', '''7d9f3304fc40182c522b531b08bff117''')],
     '''xinyang''': [('''opac/img/logo.gif''', '''de7219883618587074e9edc46e9fb6f2'''), ('''opac/css/css.css''', '''background:url(../img/an.gif)'''), ('''common/checkdata.js''', '''liuheng.200712.27:''')],
     '''zhongdongli_school''': [('''style.css''', '''url(images/zx.gif)'''),
                                                                           ('''images/zx.gif''', '''7afa5674cbcfd75b2adf2f08e7c08e07'''),
                                                                           ('''images/left3bg1.jpg''', '''c063380dec9f3bf42ea5a1b9d05e37d8'''),
                                                                           ('''images/crt.jpg''', '''e151bdbb80766bb69665fd37471712a6''')],
     '''foosun''': [('''sysImages/css/PagesCSS.css''', '''foosun'''), ('''sysImages/folder/error.gif''', '''e0a8f5ca1d3aed9dcde8aedb944dd3c1''')],
     '''liangjing''': [('''Skin/201/Style.css''', '''url(../../img/naSzarym.gif)'''), ('''Skin/201/arrow.gif''', '''913db61eeafd612522621b7c1322625f''')],
     '''jienuohan''': [('''Web/Images/ico_snap.png''', decode('\xd8)\x92O\xc6\xfc\xa8y\x8cTSK\xa2E\xd5\x95\xad\x0e\x84\\`\x88\xd7\x86Z\x18\x03^\xf7\xab\xbf\xdc')), ('''Web/Images/style.css''', '''url(ico_snap.png)''')],
     '''huashi_tv''': [('''css/login/login_bg.jpg''', '''b09e4a77678ce68bc18442804259ffd5'''), ('''uploaderv2/images/header_bg.png''', '''d0ba1fecda4c70a76926aafa107acaac''')],
     '''xiaowuyou_cms''': [('''admin/login.asp''', '''class=pwd id=VerifyCode''')],
     '''axis2''': [('''axis2/axis2-admin/login''', '''Axis2'''), ('''axis2/axis2-web/images/asf-logo.gif''', '''83fa69bb142b2d213d437be46abd64c5'''), ('''axis2/axis2-web/images/axis_l.jpg''', '''830fb825643b5996062aba8a78e3bf24''')],
     '''eduplate''': [('''Eduplate/css/css.css''', '''/images/bg_3.gif'''), ('''Eduplate/images/bg_3.gif''', '''16b15013e367f96cc0833a348231fd56''')],
     '''jeecms''': [('''r/cms/www/no_picture.gif''', '''0e932fdc5a55378ad5cac46b86b08d5b'''), ('''r/cms/head-mark1.gif''', '''65b745445ee613b4fb3f33f6bdcc3859''')],
     '''wdscms''': [('''wds_cms/admin/layout_admin.css''', '''bilder/top_bakgrund.jpg''')],
     '''iwebshop''': [('''views/default/skin/default/images/front/answer.gif''', '''2db310e263809850c45bd675482abcda'''), ('''views/default/skin/default/images/front/shadow_b.gif''', decode('\xdc)\xc4_\x84\xf4\xee.\xd2D\x1cO\xecA\xdc\xdf\xebH\xda\x0eh\xda\x91\x82R\x19U^\xa9\xe8\xe4\xc0'))],
     '''maopoa''': [('''images/favicon.ico''', '''77d3074bbc8c795c5bd7b5846cc3a84f'''), ('''images/login/maop-li.png''', '''7af705e0803fe5ba488b5d429d330eae''')],
     '''syncthru_web_service''': [('''index.html''', '''<title>SyncThru Web Service</title>'''), ('''js/cookieCode.js''', '''SetCookie ( inCookieName, inCookieValue, inCookieExpiration) '''), ('''images/samsung_logo.gif''', '''cdbad4c9b6c25ce0aedc810d3113d78a''')],
     '''shuangyang_oa''': [('''DSOA_TY/js/public.js''', '''../modules/select_more_window.aspx?name=xf.'''), ('''DSOA_TY/Images/LoginImages/deng.gif''', '''49e8f8b09b8692912e90f3d772bcde77''')],
     '''phpvibe''': [('''tpl/main/images/lang-icon.png''', '''04c21eb6971aa691184c632b79554a54'''), ('''index.php''', '''PHPVibe.com'''), ('''tpl/main/js/phpvibe_app.js''', decode('\xceb\xd2/\xc7\xf0\xf2-\xa54\x1b1\xd5=\xdf\xa9\x97x\xb8\x04\x10\xb9\xff\xb8"z-)'))],
     '''phpwiki''': [('''favicon.ico''', '''87b4e4c260ffb28a54ff5acd15a45b6f'''), ('''themes/default/phpwiki.css''', '''wikiwyg_button''')],
     '''sitefactory''': [('''sitefactory/signon.aspx?ReturnUrl=%2fsitefactory%2fdefault.aspx''', '''SiteFactory <span>CMS'''), ('''clientfiles/js/public.js''', '''assets''')],
     '''pageadmin''': [('''e/master/images/login_r2_c1.jpg''', '''cb61ba1bfef8f2c7f63f48574a777154'''), ('''e/js/lang/zh-cn.js''', '''/e/aspx/quick_login.aspx?s='''), ('''e/master/master.js''', '''PageAdmin''')],
     '''xycms''': [('''skins/images/icon-search.gif''', '''3e58d53aa94b1f2dfcf7931e4a52f510'''), ('''skins/images/more.gif''', '''c89b9f2160bb7cbdbb65260779a92dd2'''), ('''skins/green.css''', '''XYCMS''')],
     '''topsec''': [('''js/xblib.js''', '''( obj, evType, fn, useCapture, Nav4EventCode, oldHandler )'''), ('''js/exploerscss.js''', '''<LINK REL=stylesheet HREF="/site/css/main.css" TYPE="text/css">'''), ('''js/guicheck.js''', '''else if((startIP[0] == endIP[0])&& ( parseInt(startIP[1]) >  parseInt(endIP[1])))''')],
     '''strongsoft''': [('''Public/Script/VertifyForm.js''', '''zzs20100721''')],
     '''seentech_uccenter''': [('''ucenter/templates/template_1/images/dangqianweizhitubiao.gif''', '''0778ae84160ba7dc01f55f9807bf76b3'''), ('''ucenter/templates/template_1/images/main_top_left.jpg''', '''28044955ef10c4734bb8fdcfc1354f93'''), ('''ucenter/templates/template_1/images/main_top_right.jpg''', '''83a5da95f783421b1eac3e6f8aa7ee7f''')],
     '''syxxjs''': [('''images/dot.gif''', '''81b3368e33b806f09aaec682c0271381''')],
     '''kxmail''': [('''images/themeengine/10/sendmail.png''', '''e7816390288e830c40905aa3963cebd5''')],
     '''v5shop''': [('''template/skin35/images/null.gif''', '''ed280a0ea3cc38f3cbbc747acfbef47d''')],
     decode('\xc4)\xd8\x1d\xd4\xfd\xf7}\x94\x10'): [('''image/ne/feng.png''', '''66861d6c75e97c3da05a05ee10facf34''')],
     '''edayshop''': [('''inc/ys.css''', '''.djs1wz''')],
     '''xr_gatewayplatform''': [('''msa/Public/images/button_login.png''', '''96aafdbcdb17584453a4b21353339493''')],
     '''zhoupu''': [('''zhoupu/''', '''./?q=%D1%F2%C8%E2''')],
     '''powercreator''': [('''images/ICO/0/xxjl.jpg''', '''799442d902def31c8225ddcc7ed92e2a''')],
     '''esccms''': [('''Include/UserLogin.js''', '''openWindow("/OperationManage/SelectUnitMemberForLogin.aspx?name=" + account + "&unId=" + userNameId + "&upId=" + pwdId + "&param=" + param + "&divId=" + dataDivId''')],
     '''anmai''': [('''anmai/Js/CheckForm.js''', '''CopyRight By AnMai.net'''), ('''anmai/Js/comm.js''', '''5eedc1338da8eb727b338f3ed875eb2a''')],
     '''lezhixing_datacenter''': [('''datacenter/login/loginimages/bg-large1.jpg''', '''8cb2d57760718e0c8bc0cf8b52462f4b''')],
     '''kingosoft_xsweb''': [('''xsweb/images/index_border1.gif''', '''6847aab9eafaa3b18c9779ddf34f92e2''')],
     '''dianyips''': [('''dianyi/template/default/css/main.css''', '''DianyiSheji'''), ('''templates/default/css/main.css''', '''dianyisheji''')],
     '''qizhitong_manager''': [('''script/inputCheck.js''', '''IP2V(textField)'''), ('''images/u142.gif''', '''8e17dc8fdd5fdeac32447011f7c5aea6''')],
     '''yongyou_u8''': [('''pic/logo.png''', '''77725189036c03a4d2a8f49c0bc06e72'''), ('''pic/downbj.png''', '''14ef9332e4e6ceed98263347f63a6f2b'''), ('''download.php''', '''/help.php''')],
     '''workyi_system''': [('''images/admin_menu.gif''', decode('\xc8)\x8e\x01\x98\xb6\xa8a\xdaT\rV\xa2Q\x8b\xd2\xa9\x0e\xc6\x1e6\x94\x91\x82\x08F\x13Z\xff\xbb\xae\x97')), ('''content/css/global.css''', '''background:url('../images/skin.gif')''')],
     '''lianbangsoft''': [('''portal/dzjc/jsjy/images/ts_l_pic_1.jpg''', '''6da1dcbe10fcefc8737367c99b54c938''')],
     '''daiqile_p2p''': [('''bbs/main/html''', '''/bbs/main.html?q=reply'''), ('''creditshop/product/main.html''', '''daiqile_p2p'''), ('''themes/default/images/sum_bg.png''', '''95b98806a55027a15597f4507a3e13c0''')],
     '''horde_email''': [('''login.php''', '''The Horde Project''')],
     '''vbulletin''': [('''clientscript/vbulletin_md5.js''', '''hexcase'''), ('''clientscript/vbulletin_menu.js''', '''vBulletin''')],
     '''jishitongxun''': [('''images/banner.png''', '''5dd1ece04e47971bd5b97ddf2f96d934''')],
     '''yongyou_crm''': [('''about.php''', '''TurboCRM''')],
     '''yongyou_a8''': [('''seeyon/common/images/error.gif''', '''e5963ab627a547532a09c7a50470f181'''), ('''seeyon/common/js/V3X.js''', '''return "/seeyon";''')],
     '''686_weixin''': [('''tp/3/images/wdxx_ico3.jpg''', decode('\x8b)\xd4\x01\x84\xec\xb0}\x84\nOO\xaaI\xc1\xd2\xe7T\x9c\x07p\x80\x89\xccFN@O\xb5\xb7\xf8\x92'))],
     '''wdcp''': [('''images/lnamp.gif''', '''81057dac33352f7b47827b795290f613'''), ('''iProber2.php''', '''wdcp''')],
     '''pkpmbs''': [('''pkpmbs/jdmanage/loaddata.js''', '''RequestCodeData = function(code,id)'''),
                                       ('''pkpmbs/image/btnbg.gif''', '''c487f6aeb15ca18dd442910e5925d16d'''),
                                       ('''pkpmbs/manager/js/epass.vbs''', '''epsFileOffSet'''),
                                       ('''pkpmbs/html/css/login.css''', '''login p span''')],
     'humhub': [('''user/auth/login''', '''Powered by <a href="http://www.humhub.org" target="_blank">HumHub</a>'''), ('''css/animate.min.css''', '''Animate.css - http://daneden.me/animate''')],
     'rockoa': [('''webrock/css/rockcss.css''', '''rockediter_tbar'''), ('''favicon.ico''', '''c11360b62fca4129e8db0120eb7d9ce5''')],
     '''klemanndesign''': [('''script/lightbox2.4/scriptaculous.js''', '''script/lightbox2.4/effects.js'''), ('''themes/lightbox/closelabel.gif''', '''0e5462b0b4f00432eac4b33d5fa31c5a''')],
     '''yongyou_ehr''': [('''logo/images/ufida_nc.png''', '''c7cba9d9b0ff3056d56144127ff469a4''')],
     '''maticsoftsns''': [('''admin/images/logo_login.gif''', '''3c24f32ddd3df6eb423b808320f28246'''), ('''css/jquerymobile/themes/images/ajax-loader.gif''', '''08a3028fda91d443f4d5e93307c96fcd''')],
     '''igenus''': [('''images/bg.gif''', '''9667172194fa427ea477bc44898f80f1'''), ('''css/igenus.css''', '''images/bbk.gif'''), ('''images/bbk.gif''', '''b950f58e830bcb392c2d548e0027d200''')],
     '''fang5173''': [('''images/1.png''', '''a63447f0bb5cac850f7c436ccb0bcf5d'''),
                                          ('''images/index/buy.css''', decode('\x95:\x8d\t\xc6\xed\xf2\\\x85\x14I)\xf5\x1a\x8b\xc8\xbfU\x90')),
                                          ('''gameListHome.png''', '''805e7ae5bece92dd48e39d001ea36db0'''),
                                          ('''images/index/xwin.js''', '''xWin''')],
     '''phpdisk''': [('''favicon.ico''', '''297465a972da8844823361c6383ca127'''),
                                           ('''includes/js/common.js''', '''PHPDISK'''),
                                           ('''images/login_nav.gif''', '''d0eb8623e5e69148659a03ef5bc8dbc9'''),
                                           ('''includes/js/tree.js''', '''PHPDISK''')],
     '''kesioncms''': [('''ks_inc/ajax.js''', '''KesionCMS'''),
                                                ('''plus/images/rss_xml.gif''', '''035e3fb854234eb945f77ac15b52ba0c'''),
                                                ('''images/default/icon_qq.png''', '''842b4f0d9394b3fbc02e5177176201ee'''),
                                                ('''images/default/icon_qq.png''', decode('\x86)\xd8R\xd6\xec\xa5;\xd2L\x05^\xaf\x07\x87\xdf\xe3@\x94\x03h\xc6\xcb\xcc\x04\x14\x1f\r\xe3\xf1\xbb\x96')),
                                                ('''ks_inc/common.js''', '''KesionCMS''')],
     '''sdcms''': [('''theme/admin/images/line.gif''', decode('\x96)\x97_\xca\xbe\xb8i\x84\x1eWB\xbe\x0b\xd5\x95\xfa\n\x84T&\xd2\xdf\x9a\x14\x0cMZ\xfb\xbb\xae\x93')), ('''theme/admin/images/upload.gif''', '''5032b5d60b095c684fc777d7c202855e''')],
     '''zhongqidonglicms''': [('''styles/page_index.css''', '''UI CSS Frameworks Beta'''), ('''images/messages/mes-points-03.gif''', '''2897881266f0b80ef320a20ace0c62db''')],
     '''tipask''': [('''robots.txt''', '''robots.txt for TIPASK'''), ('''css/default/category_title.png''', '''795c30d270d0886d399afb38bcf0b049'''), ('''css/default/q_title.png''', '''61d5c706cd001644d79752de115223a3''')],
     '''kingdee_oa''': [('''oa/scripts/admin.js''', '''batch_do(entityName, action)'''), ('''kingdee/login/images/btn_submit.gif''', '''832e52c93417d84010cf181f8de19735''')],
     '''wizbank''': [('''cw/skin3/images/gb/css/wb_ui.css''', '''wizbank''')],
     '''soullon_edu''': [('''Content/Sites/images/favicon.ico''', '''36cdd1ce6cb153aba67fff7405be2cff''')],
     '''ewebs''': [('''images/login_03.gif''', '''3d333e088548dd32a6f0457b5d201dd3''')],
     '''gowinsoft_jw''': [('''web/web/web/images/4bt1.jpg''', '''ef1ee9c8708cde1bd25a90054de85690'''), ('''web/web/web/images/4_13.jpg''', '''577c2578f9df10fefe7aa62df1e125ae'''), ('''images/wtop.gif''', '''8f054dfdc67125dc96b209d928de0b9d''')],
     '''comexe_ras''': [('''Client/Images/comexelogo.gif''', '''55351deb29fe8890734944d5f5ece8a9'''), ('''Client/CmxBrowser.js''', '''rhawes''')],
     '''insight''': [('''csccmise/js/datetext.js''', '''onclick="fPopCalendar(datBegin,datBegin)'''),
                                           ('''csccmis/img/bottom.jpg''', '''7be7d3f55e0353f42d6ad1312c0c2a4d'''),
                                           ('''csccmis/img/12.gif''', '''96220123876034c54e562c9038f8a5a1'''),
                                           ('''csccxg/img/16.gif''', '''5914a55d8811e891001150721efa9417''')],
     '''anymacromail''': [('''help/css.css''', '''.any_table {width:90%;border-collapse:collapse}'''), ('''image/reuser.gif''', '''701829e57bb05f05a404e4dc75eafbdb''')],
     '''jinqiangui_p2p''': [('''themes/rongzi/js/base.js''', '''/plugins/?q=uploadannex'''), ('''themes/rongzi/images/lijishengji.gif''', '''b4518ab3192bad305adb39c33ecf31b3''')],
     '''uniflows''': [('''epaper/templates/blue/uniflows.css''', '''imginfo'''), ('''epaper/test/images/bg.jpg''', '''0b92c7f3dd83b49d32b91968bdd24c4b'''), ('''epaper/test/images/bg1.jpg''', '''f6224fb661ca49ded46ddb2fa270f63d''')],
     '''dswjcms''': [('''Public/js/textSlider.js''', '''textSlider.scllor''')],
     '''landray''': [('''scripts/jquery.landray.common.js''', '''".LEIS_header_nav .optionBar"'''), ('''App_Themes/Login/default/images/img_login.png''', '''b515185204249d45501d840918a3d25c''')],
     '''hishop''': [('''utility/validate/pagevalidator.js''', '''PageIsValid()'''), ('''Templates/master/default/style/validate_error.gif''', '''7daf6689abc6c1fbc8e5dc70dab4a589''')],
     '''phpb2b''': [('''robots.txt''', '''robots.txt for PHPB2B'''), ('''templates/skins/default/screenshot.jpg''', '''a322dfd639bd61a5aadc580bd8516dcd''')],
     '''3gmeeting''': [('''images/an_on.jpg''', '''f0c48c3ab92948f55bf328a2470653a6'''), ('''images/download.jsp''', '''6ac63e4862841ebb76a1954deca7f4c9''')],
     '''idvr''': [('''favicon.ico''', '''3dd2ff59ad660edc40fcd41eaf275490'''), ('''index.html''', '''iDVR Copyright'''), ('''ui/listArrow.png''', '''3d059e6b6957c1be7a1bfdb4316776e6''')],
     '''fastmeeting''': [('''images/common/xiao.gif''', '''37137658a977ed296978e2157fd018a8'''), ('''index.jsp''', '''download/FMDesktop'''), ('''images/common/logina_5.gif''', '''f8d421c34b8292352798ffdaaff83eb4''')],
     '''esafenet_dlp''': [('''CDGServer3/images/left_main.jpg''', decode('\x8e)\x82[\x88\xaa\xa4+\x84\n\x1cR\xf8\x1b\x9b\xcf\xf7\x1e\xc2T*\xd6\xdf\x9eJRIZ\xbd\xfd\xb2\xd4')), ('''CDGServer3//images/titi.gif''', decode('\x96)\x8eR\x81\xaa\xee/\xc6\x12\x01K\xfc]\xc1\x99\xf3\x1a\xcb\n6\x88\x89\xd4Z\x1d\x1fS\xf7\xf1\xae\x8e'))],
     '''atripower''': [('''Scripts/Common.js''', '''GenerateCalendar''')],
     '''uniwin_gov''': [('''styles/default/images/pos-dot.jpg''', '''48e00d58a691481ef2cc4373fcce4e44'''), ('''styles/default/images/tree-chanl.js''', '''secBoard(obj,listname,n)''')],
     '''aspcms''': [('''Templates/cn/css/styles.css''', '''wpcf7-not-valid-tip'''), ('''Templates/cn/images/top.png''', '''6cfdb244be09d237759f46298d54ca44''')],
     '''d-link''': [(decode(''), '''D-Link Systems''')],
     '''ikuai''': [(decode(''), '''ikuai'''), ('''resources/images/user_input.png''', '''149315b5919e2dc1869dc4a42bc85d84''')],
     '''ruijie_router''': [(decode(''), '''Ruijie'''), ('''free_nbr_login_skin.gif''', '''de47efc3555b788b3c636fb29d21745a'''), ('''free_login_logo.gif''', '''cd5280a35ad8410d344277b7217fc25f''')],
     '''zte''': [(decode(''), '''<title>F660</title>'''),
                           ('''img/banner.gif''', '''744230817f17c491db2d576791fba5c8'''),
                           (decode(''), '''<title>ZXV10 MS90'''),
                           ('''images/login_02.gif''', '''5e5a716c090c1e121caf3f8324527d67'''),
                           ('''images/login.jpg''', '''2e93fe9c4844f396de8ef811ce6a48d0''')],
     '''mikrotik_router''': [(decode(''), '''mikrotik''')],
     '''tp-link''': [(decode(''), '''TP-LINK Technologies Co., Ltd'''), (decode(''), '''TP-LINK''')],
     '''mpsec''': [(decode(''), '''MP1800'''), ('''webui/images/maipu/login/main_logo.png''', decode('\xd8)\x93S\xca\xec\xac;\xde\x0eC\x10\xf8\x0b\xcd\x95\xb1H\x84\\y\xc3\xd3\xc9B\x1d\x03G\xfb\xbb\xbf\x8a')), ('''images/recordBLogo.png''', '''8d1b2c65cb1ad95704af22a5147349d6''')],
     '''feiyuxing_router''': [('''scripts/webcommon.js''', '''usap_make_urlparam(element)''')],
     '''gbcom_wlan''': [(decode(''), '''http://www.gbcom.com.cn''')],
     '''jindun_gateway''': [(decode(''), '''Server: MSA/'''), ('''msa/images/main_back.gif''', '''2a89694b3901efef6695572ad9a8f9ad''')],
     '''unis_gateway''': [(decode(''), '''UF3500N'''), (decode(''), '''UF3504''')],
     '''plc_router''': [('''html/index.html''', '''PLC Systems''')],
     '''hf_firewall''': [('''images/login.gif''', '''887dadbf80b2e5f167104721bb8b66a1''')],
     '''kill_firewall''': [('''Skins/Default/Images/login_ksgv.jpg''', '''9301548af4543efc7f66b9bb300a4174''')],
     '''zhongruan_firewall''': [(decode(''), '''HuaTech-2000''')],
     '''adtsec_gateway''': [(decode(''), '''TPN-2G''')],
     '''srun_gateway''': [('''css/login.css''', '''loginbox .aboutList li''')],
     '''huachuang_router''': [('''images/login-background.jpg''', '''f5fdafef94deddde49c1e01ebd8e74a1''')],
     '''iceflow_vpn_router''': [('''images/splash.jpg''', '''a07553b9ad8a4e36380c0a33292eebab''')],
     '''bytevalue_router''': [('''images/login_map.jpg''', '''fd50ca0f27b00f87054125b0ca84807c''')],
     '''linksys''': [(decode(''), '''Basic realm="X2000"''')],
     '''mikrotik_router''': [(decode(''), '''mikrotik''')],
     '''klemanndesign''': [('''script/lightbox2.4/scriptaculous.js''', '''THE SOFTWARE IS PROVIDED "AS IS"'''), ('''themes/lightbox/closelabel.gif''', '''0e5462b0b4f00432eac4b33d5fa31c5a''')],
     '''zhuhaigaoling_huanjingzaosheng''': [('''CSS/Skins/blue/login/login.css''', '''CSS/skins/Blue/login/header.png''')],
     '''soffice''': [('''Css/office.css''', '''text2table2blue''')],
     '''cnoa''': [('''file/language/cn.js''', '''CNOA''')],
     '''jieqicms''': [('''scripts/common.js''', '''jieqi_ajax''')],
     '''natshell''': [('''images/li_r1_c1.jpg''', '''6bf253eddaf509314a51d8c9651a462c''')],
     '''zentao''': [('''favicon.ico''', '''18b786ca7913a58cb8463f1a5feca293''')],
     '''kinggate''': [('''theme/default/css/myclass.css''', '''.zr_menubutton''')],
     '''panabit''': [('''css/common.css''', '''x-grid-row-over .x-grid-cell-inner'''), ('''img/logo.gif''', '''7f2125bf1ce7f77d4a7e340a8aee0d18''')],
     '''jingci_printer''': [('''startwlm/Start_Wlm.html''', '''KYOCERA MITA''')],
     '''acsno''': [('''images_2_2/favicon.png''', '''53e754664fd16dde231fd2c1a4063997''')],
     '''yxlink''': [('''assets/style/login.css''', '''login-win .x-window-mc''')],
     '''star-net''': [('''topLogo.gif''', '''e667c02fcb1117db7ad95830938f3a95''')],
     '''netcore''': [(decode(''), '''NETCORE''')],
     '''dubbo''': [(decode(''), '''dubbo''')],
     '''shopnum1''': [('''Themes/Skin_Default/js/jquery-1.6.2.min.js''', '''Copyright 2011, The Dojo Foundation''')],
     '''mallbuilder''': [('''script/dialog/dialog.js''', '''dialog_message_contents dialog_message_notice''')],
     '''zhonghaida_vnet''': [('''CSS/default.css''', '''a:link, a:visited {color: #404040; text-decoration:none;}''')],
     '''dossm''': [('''js/dossm-global.js''', '''Dossm Global''')],
     '''haitianoa''': [('''oa/HTVOS.js''', '''function validateGoto(f)'''), ('''HTVOS.js''', '''function validateGoto(f)''')],
     '''bocweb''': [('''bocadmin/a/a.png''', '''432eb31234aa82b6bc9cb4692580c198''')],
     '''ecweb_shop''': [('''ecweb/js/common.js''', '''function returnTop(speed)''')],
     '''luepacific''': [('''webengine/images/common.css''', '''INPUT.selectobj''')],
     '''ourphp''': [('''function/plugs/layer/layer.min.js''', decode('\xe0~\xd2\x12\xc8\xfd\xfal\x92\x87\x88\xe3\xc6\x1b\x86\x83\xb3I\x95\x04\x1d\x92'))],
     '''juniper_vpn''': [('''dana-na/css/ds.js''', '''GDocumentOnKeyDown(evt)''')],
     '''xinhaisoft''': [('''style/default/style.css''', '''border: 1px solid #C2CFDF;'''), ('''xinhaisoft/style/default/style.css''', '''border: 1px solid #C2CFDF;''')],
     '''ruvarhrm''': [('''RuvarHRM/images/login_title.gif''', '''4f3ac62813564750a417a5146ac821c3'''), ('''RuvarHRM/images/logo.gif''', '''c952dc2f6134b9ef40ccf0d0a9d2f8a5'''), ('''RuvarHRM/web_login/login.aspx''', '''/RuvarHRM/script/js_window.js''')],
     '''shopnc''': [('''data/resource/js/jquery.js''', '''(function(a,b){function G(a){var b=F[a]={}''')],
     '''lvmaque''': [('''Style/Js/utils.js''', '''that.find(".navigation-list-two-con"),''')],
     '''iflytek_soft''': [('''themes/index/css/base.css''', '''color:#323232; text-decoration:none;''')],
     '''subeicms''': [('''App_Js/Common.js''', decode('\xe0~\xc5\x00\xdf\xe1\xbbS\x94\x12u\x1c\xe2\x15\x9a\x9d\xa9\x15\x88J+\x87\x9a\xb6\x08L)\t\xbd\xa5\xf0\xd1\xe2o\xd4\x0c\xdb\xfd\xffq\xa8\x1dj\x15\xf4*\xaf'))],
     '''zfsoft''': [('''style/standard/images/login_ico2.gif''', '''c48a3a6ef995859ef8bcc734d9952a99'''),
                                       ('''style/standard/module.css''', '''login_ico2.gif'''),
                                       ('''zfstyle_v4/images/login_left.jpg''', '''0b5b0a9dce12c533b375efdf5592e3e6'''),
                                       ('''zfstyle_v4/css/public.css''', '''http://www.zfsoft.com''')],
     '''qiuxue''': [('''images/ico_jt.gif''', '''d6b643474ada27843a10086416a49694'''), ('''images/b_r_btbg1.jpg''', '''39c38aee0c37c6cbc49cd3351fbf4e33'''), ('''css/global.css''', '''/images/ico_code.gif''')],
     decode('\xc4)\xdc\t\xc8\xe5\xf0o'): [('''lib/js/common.js''', '''function shooseTbody(obj)''')],
     '''trs_lunwen''': [('''paper/images/spacer.gif''', '''df3e567d6f16d040326c7a0ea29a4f41'''), ('''paper/js/go.js''', '''MM_swapImgRestore()''')],
     '''trs_ids''': [('''ids/admin/images/icon_help.gif''', '''9a63a165526a89bfa21a9db7a6d581d4'''), ('''ids/admin/js/IdSUtil.js''', '''TRS IDS''')],
     '''trs_wcm''': [('''wcm/app/js/source/wcmlib/WCMConstants.js''', '''WCM_VERSION'''), ('''common/js/com.tmd.base/common.js''', '''ajaxFormSubmit''')],
     '''trs_inforadar''': [('''inforadar/jsp/cis4/js/common/CTRSHTMLTr.js''', '''TRSHTMLTr_isInvalidElement''')],
     '''empire_cms''': [('''style/js/common.js''', '''.ico_nav_info').bind('click',function()'''), ('''nav/js/title.js''', '''className='navclose'''')],
     '''wygxcms''': [(decode('\xe0M\xfeH\xfc\xff\xfa`\x8c\x03d)\xf5\x1a\x8b\xc8\xb1B\x82'), '''blue_tit{color:#000;font-size:12px;font-weight:bold; }''')],
     '''weway_soft''': [('''Common/Main.css''', '''border:0px buttonhighlight outset;'''),
                                                    ('''crm/Common/Main.css''', '''border:0px buttonhighlight outset;'''),
                                                    ('''crm/Resources/md5/md5.js''', '''CryptoJS=CryptoJS'''),
                                                    ('''Resources/md5/md5.js''', '''CryptoJS=CryptoJS''')],
     '''terramaster''': [('''css/common.css''', '''input:-moz-placeholder{color:#A9A9A9;}''')],
     '''edusohocms''': [('''assets/libs/seajs-global-config.js''', '''edusoho''')],
     '''kj65n_monitor''': [('''images/login/css.css''', '''COLOR: #000000; TEXT-DECORATION: underline''')],
     '''electric_monitor''': [(decode(''), '''MM_swapImage()''')],
     '''hac_gateway''': [('''login.php''', ''' HACClientSignByKey''')],
     '''xplus''': [('''static/images/index/logo.png''', '''1e92bc4b9967b3e562e34a817759c407''')],
     '''dahua_dss''': [('''portal/include/script/dahuaDefined/headCommon.js''', '''By HanLulu''')],
     '''acsoft''': [('''images/tagright.gif''', '''2af1905871bb3464a712d73aa6460bb0''')],
     '''shop7z''': [('''index_ad.css''', '''www_zzjs_net_box ul''')],
     '''enjie_soft''': [('''fo/flash.js''', '''flashToElem:function (elem)''')],
     '''totalsoft_lib''': [('''pic/BTLogin.jpg''', '''7fb5e572548e01b47b0c9cc763224d76'''), ('''pic/BTReset.jpg''', '''f820a3525f4f8a3eb80e847fc03d5dae''')],
     '''1039_jxt''': [('''images/jxt_logo.gif''', '''d9a4ebcfc4eec9120f881224b9768e2c'''), ('''css/stuselect/index.css''', '''height: 35px; position: relative''')],
     '''xuezi_ceping''': [('''ceping/images/hou_06.jpg''', '''c8b502aec715fd6f732fe2d2eb02f2f9'''), ('''ceping/images/login.jpg''', '''233df380afc2dcfb2ad0691966a6b293''')],
     '''skytech''': [('''jyweb/inc/comm.js''', '''OpenAttachmentWindow(url)'''),
                                           ('''inc/comm.js''', '''OpenAttachmentWindow(url)'''),
                                           ('''jyweb/img/index/b7.gif''', '''6f119cf41b434479984746c041cd6679'''),
                                           ('''img/index/b7.gif''', '''6f119cf41b434479984746c041cd6679''')],
     '''sztaiji_zw''': [('''images/tb3.png''', '''35bbd07154ea86ea80350d2d7dcf04ca'''), ('''css/head.css''', '''background-image: url(/images/index/Tab1.gif);''')],
     '''dfe_scada''': [('''index.php''', '''Dongfang Electronics Co., Ltd.'''), ('''modules/authen/js/login.js''', '''"dfnewweb_ifsavepwd",ifsavepwd,getExpDate(365,0,0));'''), ('''images/seperator.jpg''', '''d155cd5eeb8a1fdb345e572c3aacab95''')],
     '''lebishop''': [(decode(''), '''Powered by LebiShop'''),
                                            ('''ajax/js.aspx''', '''function Tag(strin)'''),
                                            ('''admin/images/login/submit.jpg''', '''0b9e405e740e92fcbb75a4b72ed9073b'''),
                                            ('''theme/system/images/load.gif''', '''24e39c39bd311ff27fee252583e3a706''')],
     '''shenlan_jiandu''': [('''image_new/mid9.gif''', '''e1d31751042eebbd5e5202ae99bb2ec7'''), ('''images/arr.gif''', '''1f0be5d2323f66b3e076897bc8ddd3a8''')],
     '''tianrui_lib''': [('''tushu/imgs/s-button.jpg''', '''34cfd1e1a4d645efc8ef3f716526be8b'''),
                                                     ('''imgs/s-button.jpg''', '''34cfd1e1a4d645efc8ef3f716526be8b'''),
                                                     ('''tushu/imgs/s-6.jpg''', '''e8e80bf5e059ca96445229b0cb8d9257'''),
                                                     ('''tushu/imgs/index.css''', '''id_FIJ_R_ImgBlk'''),
                                                     ('''imgs/index.css''', '''id_FIJ_R_ImgBlk''')],
     '''qht_study''': [('''Js/exam.js''', '''AddExam_type(pmid)''')],
     '''sgc8000''': [('''sgc8k_map/''', '''SGC8000''')],
     '''weblogic''': [('''uddiexplorer/''', '''Weblogic''')],
     '''seagate_nas''': [(decode(''), '''Seagate NAS''')],
     '''netpower''': [('''direct/api.php''', '''Ext.ns('Ext.Netpower')''')],
     '''s8000''': [('''asp/Style/Style.css''', '''word-break:break-all;''')],
     '''net110''': [('''css/pub.css''', '''pubNormalTitleGroup_2''')],
     '''netoray_nsg''': [('''scripts/webcommon.js''', '''create field save access infomation''')],
     '''canon''': [('''media/canonlogo.gif''', '''933604a1dd77d324af0d5ac633931690''')],
     '''aten_kvm''': [('''img/top_logo.gif''', '''6b327a45dfcd635a00b8712bdf6c11d9''')],
     '''yuanwei_gateway''': [('''images/dl.gif''', '''c9c36803926544f57810598d16f2c8f9'''), ('''images/zp/home.png''', '''09f7d8a2198c9eb6785d01a0584cc359''')],
     '''dreamgallery''': [('''dream/css/gallery.css''', '''Courgette'''), ('''dream/js/fancy/jquery.fancybox.css?v=2.1.0''', '''Helvetica Neue''')],
     '''shadows-it''': [('''css/shadows_it.css''', '''MENU_HEADER_R''')],
     '''hsort''': [('''images/news.jpg''', '''3d6cdd96fd7fc2d37221d62eb89b15dc''')],
     '''house5''': [('''statics/house5-style1/index/css/reset.css''', '''main{width:960px;margin:0 auto;}''')],
     '''gooine_sqjz''': [('''inc/sqjz.css''', '''span.pop_message:hover''')],
     '''bohoog''': [('''JavaScript/script.js''', '''myAnchors=document.all.tags("A")''')],
     '''visionsoft_velcro''': [('''vjs/sack.js''', '''Simple AJAX Code-Kit (SACK)''')],
     '''zdsoft_cnet''': [('''cnet/system/login.jsp''', '''ZDSOFT.NET'''), ('''cnet/template/1/common.css''', '''modelno{''')],
     '''ltpower''': [('''Content/css/common.css''', decode('\xc4q\xc9\x1a\xd2\xfd\xe8o\x91\x1e\\C\xed\x16\x8e\x94\xa4X\xd9L/\x99\xcb\x87S\x1e\x06\t\xbc\xb3\xfd\xc2\x87)\x93\x17\xc1\xb7')), ('''Content/images/warning.png''', '''15faac1c7ed012854aec8f3973f2d481''')],
     decode('\xd6)\xef\x19\xdf\xe1\xfey\x8a\x0eB\x04\xfc'): [('''Conf/images/lock.gif''', '''7cd79158f68197deaa7a27bc9d2bca8f'''), ('''Conf/images/titelbkg.gif''', '''9f11dc6b4eae977270d363feed0c151a''')],
     '''smart_oa''': [('''content/images/headerback.jpg''', '''674784f372f603436befd992f90fdd64'''), ('''content/theme/base.css''', '''iepngfix, img, .menu-item-line''')],
     '''moxa_nport_router''': [('''logo.gif''', '''27829d70bb23c465d86b9c643cf534d3''')],
     '''nanjing_shiyou''': [('''images/css.css''', '''copyrightDIV''')],
     '''zf_cms''': [('''cms/js/tab.js''', '''Designer X.Wong''')],
     '''kingdee_eas''': [('''easweb/cp/stamp/res/CheckIEUtils.js''', '''showEachClientCheckResult''')],
     '''rockontrol''': [('''plugins/login/css/rklogin.css''', '''background-repeat: no-repeat;'''), ('''plugins/login/images/login_logo.jpg''', '''73d39a88da649fb3b2150b58fa6dd8fe''')],
     '''nitc''': [('''js/search.css''', '''autocompletepanel'''), ('''fl_en.gif''', '''6368b440f28ecb8d312df38b8cd80a90''')],
     '''mainone_b2b''': [('''JS/TreeView.js''', '''TreeView_ClickNode(node,children''')],
     '''huanet''': [('''huanet/Admin_Style.css''', '''Images/TxtRule.jpg''')],
     '''looyu_live''': [('''live/lang/sc.js''', '''msgUploadErrorType''')],
     '''ruvar_oa''': [('''script/js_common.js''', '''GetQueryString(querystring)''')],
     '''ynedut_campus''': [('''skin/color1/css/common.css''', '''author: HeQiang''')]}
    if 0:
        i11iIiiIii / IIii1I.I11i % iII111i / II1 % Ii1I
    o0ooo00O0o0 = {}
    for o0Oo00OOOOO in [OOooO0OOoo, iI111I11I1I1]:
        O0O = o0Oo00OOOOO == iI111I11I1I1
        for O00o0OO in o0Oo00OOOOO:
            I11i1 = o0Oo00OOOOO[O00o0OO]
            for iIi1ii1I1 in I11i1:
                if isinstance(iIi1ii1I1, tuple):
                    o0, I11II1i = iIi1ii1I1
                else:
                    o0, I11II1i = iIi1ii1I1, None
                if not isinstance(o0, list):
                    o0 = [o0]
                for IIIII in o0:
                    if IIIII not in o0ooo00O0o0:
                        o0ooo00O0o0[IIIII] = []
                    o0ooo00O0o0[IIIII].append((O00o0OO, I11II1i, O0O))
                    if 0:
                        iIiiiI1IiI1I1 % iIiiiI1IiI1I1

    iI1 = o0ooo00O0o0.keys()
    iI1.sort(key=len)
    if 0:
        IiII + IIII
    Oo0Ooo = False
    ooo = False
    if 0:
        OOooOOo
    if 0:
        iII111i - o00O0oo.o00O0oo + oO0o - II1 + OOO0O0O0ooooo
    for o0 in iI1:
        for oOoOooOo0o0, I11II1i, O0O in o0ooo00O0o0[o0]:
            if 0:
                OOooOOo / Ooo00oOo00o + IIII * Ii1I / Ii1I
            if not O0O:
                oO000OoOoo00o, iiiI11, OOooO = oo0ooO0oOOOOo(i1iIIi1 + o0)
                if OO0o(o0, oOoOooOo0o0, I11II1i, O0O, OOooO, oO000OoOoo00o, i1iIIi1, iiiI11):
                    ooo = True

        if ooo:
            break

    for o0 in iI1:
        for oOoOooOo0o0, I11II1i, O0O in o0ooo00O0o0[o0]:
            if O0O:
                oO000OoOoo00o, iiiI11, OOooO = oo0ooO0oOOOOo(i1iIIi1 + o0)
                OO0o(o0, oOoOooOo0o0, I11II1i, O0O, OOooO, oO000OoOoo00o, i1iIIi1, iiiI11)
                if 0:
                    O00ooooo00 / II1 - OOO0O0O0ooooo / oO0o.iIiiiI1IiI1I1 - O00ooooo00
                if 0:
                    iII111i + I1Ii111 * iII111i - Ooo00oOo00o * OOooOOo


if __name__ == '__main__':
    import urllib
    from dummy import *
    if 65 - 65:
        OOO0O0O0ooooo % IIiIiII11i.I11i % IIii1I / iII111i % oO0o0ooO0
    if 51 - 51:
        i11iIiiIii.IIiIiII11i + iIiiiI1IiI1I1
    if 10 - 10:
        I11i * IIII * iIiiiI1IiI1I1 % I1Ii111.iII111i + oO0o0ooO0
    if 19 - 19:
        oO0o - IIiIiII11i.iII111i / o00O0oo
    if 33 - 33:
        oO0o0ooO0 / I11i % IIiIiII11i + IIII / Ooo00oOo00o
    if 52 - 52:
        OOooOOo - II1 + I1Ii111 + I1Ii111 - OOooOOo / oO0o0ooO0
    if 44 - 44:
        IIII.O00ooooo00 - I11i.OOO0O0O0ooooo - IIII
    if 92 - 92:
        ooOoO0o.IiII + OOooOOo
    if 28 - 28:
        O00ooooo00 * IiIIi1I1Iiii - OOooOOo * o00O0oo * I1Ii111 / Ooo00oOo00o
    if 94 - 94:
        iIiiiI1IiI1I1 % I11i / oO0o * IIii1I
    if 54 - 54:
        OOooOOo - IIiIiII11i + II1
    if 70 - 70:
        I1Ii111 / IiII.ooOoO0o % IiIIi1I1Iiii
    if 67 - 67:
        oO0o * OOooOOo.o00O0oo - Ooo00oOo00o * OOooOOo
    IIiI1I = [decode('\xcdq\xc2\x17\x89\xa5\xbb7\xc6C\x1d^\xb2V\xd5\xdf\xfa\x15\xcf\x0eu\xc7\x85\xc9^\x03\t\x13\xe4')]
    for i1iIIi1 in IIiI1I:
        O00Oo000ooO0 = assign('''www''', i1iIIi1)[1]
        if type(O00Oo000ooO0) == str:
            O00Oo000ooO0 = [O00Oo000ooO0]
        for OoO0O00 in O00Oo000ooO0:
            if 5 - 5:
                IiIIi1I1Iiii / OOooOOo.I1Ii111 - OOO0O0O0ooooo / o00O0oo
            audit(OoO0O00)
            if 62 - 62:
                IIii1I * oO0o
            if 26 - 26:
                ooOoO0o.oO0o0ooO0
            if 68 - 68:
                Ooo00oOo00o

#KEY---ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0---