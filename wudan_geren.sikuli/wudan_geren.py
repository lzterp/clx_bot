import random

#global variable
men_pai = None

#清理满屏
def refresh_main():
    click(Location(1819, 104))
    wait(1)
    mapclose = exists("1555907993509.png")
    if mapclose:
        click(mapclose)

def confirm_check():
    ge_ren_confirm = exists("1555910648795.png")
    if ge_ren_confirm:
        click(ge_ren_confirm)    

def enter_huo_dong():
    wait(1)
    activity = exists("1555907705355.png")
    if activity:
        click(activity)

def enter_hang_dang():
    hang_dang_off = exists("1556075962049.png")
    if hang_dang_off:
        click(hang_dang_off)

def enter_jiang_hu():
    jiang_hu = exists("1556769526168.png")
    
    if jiang_hu:
        click(jiang_hu)

def qian_wang():
    click("1555908648951.png")      
    wait(1)
    confirm_qian_wang = exists("1555909003307.png")
    if confirm_qian_wang:
        click(confirm_qian_wang)
    wait(5)

def loop_check(img_target, times = 20, raise_error = True):
    max_retry = times
    img_start = exists(img_target)
    while not img_start:
        wait(10)
        img_start = exists(img_target)
        max_retry = max_retry - 1
        if max_retry == 0:
            if raise_error:
                raise Exception('image target should have been found')
            else:
                return 0
    click(img_start)

def ti_jiao():
    ge_ren_purchase = exists("1556059325267.png")
    if ge_ren_purchase:
        click(ge_ren_purchase)
    
refresh_main()

#进入活动
enter_huo_dong()

#算命
you_li_menu_off = exists("1556768004209.png")
if you_li_menu_off:
    click(you_li_menu_off)
wait(1)
shuan_ming = exists("1556768124212.png")

if shuan_ming:
    print("shuang ming found")
    click(shuan_ming)
    qian_wang()
    loop_check("1556768421023.png")
    wait(1)
    click("1556768484262.png")
    max_height = 768
    min_height = 288
    max_width = 1413
    min_width = 521
    height1 = random.randrange(min_height, max_height)
    height2 = random.randrange(min_height, max_height)
    height3 = random.randrange(min_height, max_height)
    width1 = random.randrange(min_width, max_width)
    width2 = random.randrange(min_width, max_width)
    width3 = random.randrange(min_width, max_width)
    dragDrop( Location(width1, height1), Location(width2, height2))
    dragDrop( Location(width2, height2), Location(width3, height3))
    click("1556769057340.png")
    wait(1)
    click("1556769083581.png")
    wait(1)
    confirm_check()
    wait(1)
    refresh_main()
     
#算命完成
#课业
wait(1)
enter_huo_dong()
wait(1)
enter_jiang_hu()
ke_yi = exists("1555989218071.png")
if ke_yi:
    print("wu dang found")
    men_pai = "WuDang"
    click(ke_yi)
    wait(1)
    qian_wang()
    loop_check("1555989558087.png",20,False)
#选难的
    hard_key_yi = exists("1555909753530.png")
    refresh_tries = 5
    while not hard_key_yi and refresh_tries > 0:
        click("1555909776671.png")
        wait(1)
        click("1556058744449.png")
        wait(1)
        
        hard_key_yi = exists("1555909753530.png")
        refresh_tries = refresh_tries - 1
    if hard_key_yi:
        click(hard_key_yi)

    loop_count = 0

    while loop_count < 8:
        print("Wait Ke Yi Event")
        wait(60)
        #问答
        ge_ren_wen_da = Region(1740,198,154,37)
        maxloop = 10
        while ge_ren_wen_da.exits("1556171177430.png") and maxloop> 0:
            click(Location(1553, 316))
            wait(2)
            maxloop = maxloop - 1
        ti_jiao()
                 
        ge_ren_goumai = exists("1555910620958.png") 
        while ge_ren_goumai:
            click(ge_ren_goumai)
            wait(1)
            click("1556059218727.png")
            wait(10)
            ge_ren_purchase = exists("1556059325267.png")
            if ge_ren_purchase:
                click(ge_ren_purchase)
            else:
                #刷到任务栏
                click(Location(31, 268))
                wait(1)
                click(Location(235, 198))
                wait(1)
                click(Location(222, 310))
                wait(1)
                ge_ren_goumai = exists("1555910620958.png") 
            confirm_check()
   
        loop_count = loop_count + 1
check_ke_yi_complete = exists("1556061316177.png")
if check_ke_yi_complete:
    men_pai = "WuDang" 
#课业结束    
#帮派开始
enter_huo_dong()
bang_pai_menu_off = exists("1556065352531.png")
if bang_pai_menu_off:
    click(bang_pai_menu_off)

bangpai_region = Region(253,268,149,128)
if bangpai_region.exists("1556073702671.png"):
    click(bangpai_region)

    qian_wang()
    loop_check("1556072458791.png")
    confirm_check()
    loop_check("1556074355535.png", 30, False)
    print("complete bang pai xu qiu")
    wait(2)
    click(Location(1273, 856))
    wait(10)
    ti_jiao()
#帮派结束           
refresh_main()

#白帮
enter_huo_dong()
wait(1)
enter_hang_dang()
wait(1)
bai_bang_region = Region(1465,279,141,129)
if bai_bang_region.exists("1556076278638.png"):
    click(bai_bang_region.offset(0,120))
    loop_check("1556076399744.png")
    wait(2)
    jie_bang = exists("1556076529190.png")
    if jie_bang:
        click(jie_bang)
    
    
    
            



