var btnLoadmore;
var progress;
var currentProds;
var allProds;

var existsMoreItems = function(){
	progress = document.getElementsByClassName("prodlist__progress-count")[0].innerHTML.split(' ');
	currentProds = parseInt(progress[0]);
	allProds = parseInt(progress[3]);
	return currentProds < allProds;
}

var load = function(){
	btnLoadmore = document.getElementsByClassName("prodlist__loadmore-btn")[0];
	let moreItems = existsMoreItems();
	if(moreItems && !btnLoadmore.classList.contains("loading")){
		btnLoadmore.click();
	} else if (moreItems && btnLoadmore.classList.contains("loading")){
		setTimeout(load, 3000);
	} else {
		new new;
	}
}