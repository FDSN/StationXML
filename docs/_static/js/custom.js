//alert("here");

window.onload = function(){
  //changing download link to the current version
  var version=$(".version").text().trim();
  var downloadVersion="https://stationxml-doc.readthedocs.io/_/downloads/en/"+version+"/pdf/";

  console.log(downloadVersion);

  //navbar
  var toChange=$("body > div.wy-grid-for-nav > nav > div > div.wy-menu.wy-menu-vertical > ul > li > a:contains(Download PDF)");

  //index page
  var toChange1=$("#welcome-to-stationxml-docs-s-documentation > div > ul > li > a:contains(Download PDF)");
  var toChange2=$("#indices-and-tables > ul > li > p > a:contains(Download PDF)");

  toChange.attr('href',downloadVersion);
  toChange1.attr('href',downloadVersion);
  toChange2.attr('href',downloadVersion);


// cache the navigation links
var $navigationLinks = $('.reference.internal');

// cache (in reversed order) the sections
var $sections = $($(".headerlink").get().reverse());



// map each section id to their corresponding navigation link
var sectionIdToNavigationLink = {};
$sections.each(function() {

    var href = $(this).attr('href');
    sectionIdToNavigationLink[href] = $('.reference.internal[href=\\' + href + ']');

});



//below here works
function highlightNavigation(decimalOff) {

    // get the current vertical position of the scroll bar, along with the document and window's height
    var scrollPosition = $(window).scrollTop();
    var documentHeight=$(document).height();
    var windowHeight=$(window).height()

    // iterate the sections
    $sections.each(function() {
        var currentSection = $(this);
        // get the position of the section
        var sectionTop = currentSection.offset().top;

        //when you are near the very top of the document, you will select the top one automatically
        if (scrollPosition<windowHeight*.2){
          setCurrents($sections.eq(-2));
          return false;
        }

        //how much away from the top of the screen it will be
        var offset=windowHeight*decimalOff;


        // if the user has scrolled over the top of the section, or if at very bottom of page
        if (scrollPosition+offset >= sectionTop || documentHeight==scrollPosition+windowHeight) {

            setCurrents(currentSection);
            return false;
        }

    });
    //console.log("nothing here!")

}

function setCurrents(currentSection){
  var href = currentSection.attr('href');
  // get the corresponding navigation link
  var $navigationLink = sectionIdToNavigationLink[href];
  //console.log($navigationLink)


  //sections
  /*
  $('.headerlink').parent().removeClass('current-section');
  currentSection.parent().addClass('current-section');
  */

  //if section isn't already current, set it to be
  if (!$navigationLink.parent().hasClass('current')&&$navigationLink.length) {
      //navigation
      $(".reference.internal").parent().removeClass('current');
      addCurrent($navigationLink);

    }
}

//add current to class and its parents
function addCurrent(navLink){
          navLink.parent().addClass('current');

          //finds the next one up
          var parentNavLink=navLink.parent().parent().siblings(".reference.internal");
          if (parentNavLink.length==1){
            addCurrent(parentNavLink);
      }
}




$(window).scroll( function (){highlightNavigation(.15) });

}
