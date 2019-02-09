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

const options = {
  shouldSort: true,
  threshold: 0.6,
  location: 0,
  distance: 100,
  maxPatternLength: 32,
  minMatchCharLength: 1,
  keys: [
    "organization",
    "name"
  ]
}

const fuse = new Fuse(events, options)


function filterByOrg() {
    const query = $('#orgSearch').val()
    
   
    const result = fuse.search(query);

    let show = []
    for (const i in result) {
           show.push(result[i].slug)
    }

    console.log(show)

    $('.event-block').each(function(){
        skip = false
        for (const i in show ) {
             if ($(this).hasClass(show[i])) {
                skip = true
             }
        }
        if (!skip) {
            $(this).css('display', 'none')
        } else {
            $(this).css('display', 'inline-block')
        }
       
    })
}








