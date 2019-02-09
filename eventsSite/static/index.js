let MOBILE = false

$(document).ready(function(){
    if ($(window).width() < 900 ) {
        MOBILE = true
    } else {
        MOBILE = false
    }
    checkWindowSizeAdjustSidebar()
})


$(window).resize(function(){
    if ($(window).width() < 900 ) {
        MOBILE = true
    } else {
        MOBILE = false
    }
    checkWindowSizeAdjustSidebar()
})


function checkWindowSizeAdjustSidebar() {
    $('#sidebar-icon').css('display', 'inline-block')
    if (MOBILE) {
        closeSidebar()
    } else {
        $('#sidebar-icon').css('display', 'none')
        openSidebar()
    }
}

function toggleSidebar() {
    if ($('#sidebar').hasClass('hidden') && MOBILE) {
        openSidebar()
    } else if (MOBILE) {
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

const placeSearchOptions = {
    shouldSort: true,
    tokenize: true,
    includeScore: true,
    threshold: 0.6,
    location: 0,
    distance: 100,
    maxPatternLength: 32,
    minMatchCharLength: 1,
    keys: [
    "location"
    ]
}

const topicSearchOptions = {
    shouldSort: true,
    tokenize: true,
    includeScore: true,
    threshold: 0.6,
    location: 0,
    distance: 100,
    maxPatternLength: 32,
    minMatchCharLength: 1,
    keys: [
    "name"
    ]
}

const orgSearchOptions = {
    shouldSort: true,
    tokenize: true,
    includeScore: true,
    threshold: 0.6,
    location: 0,
    distance: 100,
    maxPatternLength: 32,
    minMatchCharLength: 1,
    keys: [
    "organization"
    ]
}

function filterEventBlocks(show) {

    $('.col-hlder').each(function(){
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

function filterByOrg() {
    const query = $('#orgSearch').val()
    const fuse = new Fuse(events, orgSearchOptions)
    const result = fuse.search(query);

    let show = []
    for (const i in result) {
        if (result[i].score < 0.4){
           show.push(result[i].item.slug)
        }
    }

    filterEventBlocks(show)
    toggleSidebar()
}

function showAllEvents() {
    $('.col-hlder').each(function(){
        $(this).css('display', 'inline-block')
       
    })
    $('#orgSearch').val("")
    $('#placeSearch').val("")
    $('#topicSearch').val("")
    toggleSidebar()
}

function showOrgs() {
    const orgs = userOrgs[0].organizations

    let show = []

    for (const i in orgs) {
        for (const j in events) {
            if (events[j].organization == orgs[i]) {
                show.push(events[j].slug)
            }
        }
    }

    filterEventBlocks(show)
    toggleSidebar()
}

function filterByPlace() {
    const query = $('#placeSearch').val()
    const fuse = new Fuse(events, placeSearchOptions)
    const result = fuse.search(query);

    let show = []
    for (const i in result) {
        if (result[i].score < 0.4){
           show.push(result[i].item.slug)
        }
    }

    filterEventBlocks(show)
    toggleSidebar()

}


function filterByTopic() {
    const query = $('#topicSearch').val()
    const fuse = new Fuse(events, topicSearchOptions)
    const result = fuse.search(query);

    let show = []
    for (const i in result) {
        if (result[i].score < 0.4){
           show.push(result[i].item.slug)
        }
    }

    filterEventBlocks(show)
    toggleSidebar()

}











