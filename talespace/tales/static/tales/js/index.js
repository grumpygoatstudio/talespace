var stepSlider,
activeStep,
talesOpen = false;
var app = [];
var appdata = {
		showMenu: true,
		currentView: 'home',
		user:[{
			name: '',
				
		}],
		
	};



// Setting up view components for Vue
const home= {
	template: '',
	data: function() {
	    return appdata;
	},
	mounted:function(){
		console.log('f');
		slidr.create('home-slider', {
	  breadcrumbs: true,
	  controls: 'border',
	  direction: 'horizontal',
	  fade: true,
	  keyboard: true,
	  overflow: true,
	  theme: '#fff',
	  touch: true,
	  transition: 'fade'
	}).start().auto(6000);	
	
	
	stepSlider = slidr.create('step-slider', {
	  breadcrumbs: false,
	  controls: 'none',
	  direction: 'horizontal',
	  fade: false,
	  keyboard: true,
	  overflow: true,
	  theme: '#fff',
	  touch: true,
	  transition: 'fade'
	}).start();

	$('.open-popup-link').magnificPopup({type:'inline',
		  removalDelay: 300,
  mainClass: 'mfp-fade'
	});
		$('[data-steptrigger]').on('mouseover', function(){
			activeStep = $(this).attr('data-steptrigger');
			stepSlider.slide(activeStep);
		
			$('[data-steptrigger]').each(function(){
				$(this).removeClass('active');
			});
			$(this).addClass('active');
		});
		
		$('.tales-trigger').on('click', function(){
			if(talesOpen){
				$(this).html('Explore all tales');
				talesOpen = false;
			} else {
				$(this).html('Close all tales');
				talesOpen = true;
			};
			$('.tales-container').toggle(500);
		});
		
		//Question handler
	  	$('li.q').on(action, function(){
		  //gets next element
		  //opens .a of selected question
		  $(this).next().slideToggle(speed).siblings('li.a').slideUp();
		  
		  //Grab img from clicked question
		var img = $(this).children('img');
		  //Remove Rotate class from all images except the active
		  $('img').not(img).removeClass('rotate');
		  //toggle rotate class
		  img.toggleClass('rotate');
	
	 
		});//End on click

	}
 };
 const story= {
	template: '#page-story-accounting',
	data: function() {
	    return appdata;
	},
	mounted: function(){
			$('.open-popup-link').magnificPopup({type:'inline',
		  removalDelay: 300,
  mainClass: 'mfp-fade'
	});
	}
 };
  const profile= {
	template: '#page-profile',
	data: function() {
	    return appdata;
	},
	mounted: function(){
		console.log('eed');
		  $('#magicSuggest').magicSuggest({
    	});
	}
 };

const reading = {
	template: '#page-story-reading',
	data: function() {
	    return appdata;
	},
	mounted: function(){
			$('.open-popup-link').magnificPopup({type:'inline',
		  removalDelay: 300,
  mainClass: 'mfp-fade'
	});
	}
 };

// Starting router
const routes = [
  { path: '/', component: home},
  { path: '/story/1/:storyName', component: story},
  { path: '/story/2/:storyName', component: reading},
  { path: '/profile', component: profile},
]
const router = new VueRouter({
  routes,
  linkActiveClass: 'is-active'
});
router.beforeEach(function (to, from, next) {
  window.scrollTo(0, 0)
  next();
})
//Accordian Action
var action = 'click';
var speed = "500";


//Document.Ready
$(document).ready(function(){
	// Setup 

	// Setup sliders
	/*slidr.create('home-slider', {
	  breadcrumbs: true,
	  controls: 'border',
	  direction: 'horizontal',
	  fade: true,
	  keyboard: true,
	  overflow: true,
	  theme: '#fff',
	  touch: true,
	  transition: 'fade'
	}).start().auto(6000);	
	
	slidr.create('tagline-slider', {
	  breadcrumbs: false,
	  controls: 'none',
	  direction: 'horizontal',
	  fade: false,
	  keyboard: true,
	  overflow: true,
	  theme: '#fff',
	  touch: true,
	  transition: 'fade'
	}).start().auto(3000);
	
	stepSlider = slidr.create('step-slider', {
	  breadcrumbs: false,
	  controls: 'none',
	  direction: 'horizontal',
	  fade: false,
	  keyboard: true,
	  overflow: true,
	  theme: '#fff',
	  touch: true,
	  transition: 'fade'
	}).start();
*/
	
	/*$('[data-steptrigger]').each(function(){

	  	//stepSlider.slide('teach');
	  	$(this).on('hover', function(){
		  	console.log('holla'+$(this).attr('data-steptrigger'));
	  	});
	  	
	  	//  	$(this).attr('data-steptrigger');
	});*/
	

	app = new Vue({
	  router,
      el: '#app',
      appdata
	});
	

});//End Ready
function closePopup() {
  $.magnificPopup.close();
}

