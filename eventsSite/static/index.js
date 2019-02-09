$(document).ready(function(){
    checkWindowSizeAdjustSidebar()
})


$(window).resize(function(){
    checkWindowSizeAdjustSidebar()
})


function checkWindowSizeAdjustSidebar() {
    $('#sidebar-icon').css('display', 'inline-block')
    if ($(window).width() < 900 ) {
        closeSidebar()
    } else {
        $('#sidebar-icon').css('display', 'none')
        openSidebar()
    }
}

function toggleSidebar() {
    if ($('#sidebar').hasClass('hidden')) {
        openSidebar()
    } else {
        closeSidebar()
    }
}

function closeSidebar() {
    $('#sidebar').addClass('hidden')
    $('#scroll-content').css('padding-left', '0')
    $('#scroll-content').css('width', ($(window).width()).toString() + 'px')
}

function openSidebar() {
    $('#sidebar').removeClass('hidden')
    $('#scroll-content').css('padding-left', '375px')
    $('#scroll-content').css('width', 'calc(100vw - 375px)')
}