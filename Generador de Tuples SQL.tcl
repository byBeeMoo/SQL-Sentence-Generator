#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Jan 30, 2020 08:44:42 PM CET  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}



    menu .pop53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont -foreground black \
        -tearoff 0 
    vTcl:DefineAlias ".pop53" "Popupmenu1" vTcl:WidgetProc "" 1
    menu .pop54 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont -foreground black \
        -tearoff 0 
    vTcl:DefineAlias ".pop54" "Popupmenu2" vTcl:WidgetProc "" 1

proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m60" -relief groove -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 600x450+342+141
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1265 877
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra44 \
        -borderwidth 1 -relief sunken -background $vTcl(actual_gui_bg) \
        -height 35 -width 205 
    vTcl:DefineAlias "$top.fra44" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra44
    label $site_3_0.lab47 \
        -activebackground #ededed -activeforeground #fcfcfc \
        -background #d8d8d8 -borderwidth 2 \
        -font {-family {Liberation Serif} -size 12} \
        -foreground $vTcl(actual_gui_fg) -text {Generador de tuples SQL} 
    vTcl:DefineAlias "$site_3_0.lab47" "HeaderLabel" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab47 \
        -in $site_3_0 -x 10 -y 8 -width 186 -relwidth 0 -height 18 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.fra55 \
        -relief groove -background #93d8ba -height 455 -width 35 
    vTcl:DefineAlias "$top.fra55" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    frame $top.fra56 \
        -relief groove -background #93d8ba -height 35 -width 605 
    vTcl:DefineAlias "$top.fra56" "Frame3" vTcl:WidgetProc "Toplevel1" 1
    frame $top.fra58 \
        -relief groove -background #93d8ba -height 455 -width 35 
    vTcl:DefineAlias "$top.fra58" "Frame4" vTcl:WidgetProc "Toplevel1" 1
    frame $top.fra59 \
        -relief groove -background #93d8ba -height 25 -width 615 
    vTcl:DefineAlias "$top.fra59" "Frame5" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m60
    menu $site_3_0 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra44 \
        -in $top -x 180 -y 25 -width 205 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra55 \
        -in $top -x -20 -y 0 -width 35 -relwidth 0 -height 455 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra56 \
        -in $top -x 0 -y -20 -width 605 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra58 \
        -in $top -x 585 -y 0 -width 35 -relwidth 0 -height 455 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra59 \
        -in $top -x 0 -y 435 -width 615 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

