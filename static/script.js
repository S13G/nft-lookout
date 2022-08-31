const listing_btn = document.getElementById("listing");
const listing_form = document.querySelector(".popup");
const close_listing = document.getElementById("close");

window.onload = function exampleFunction() {
  darkbtn.toggle();
};

listing_btn.onclick = () => {
  listing_form.classList.toggle("shown");
  menu_item.classList.remove("active");
};

close_listing.onclick = () => {
  listing_form.classList.remove("shown");
};

const menu = document.querySelector(".fa-bars");
const menu_item = document.querySelector(".website .left");
const close_nav = document.querySelector(".nav_close");

menu.onclick = () => {
  menu_item.classList.toggle("active");
};

close_nav.onclick = () => {
  menu_item.classList.remove("active");
};

const options = {
  bottom: "20px",
  right: "20px",
  left: "unset",
  time: "0.5s",
  mixColor: "#fff",
  backgroundColor: "#fff",
  saveInCookies: true,
  label: "🌙",
  autoMatchOsTheme: true,
};

const darkmode = new Darkmode(options);

const darkbtn = document.getElementById("dark_btn");

darkbtn.onclick = () => {
  console.log(darkmode.isActivated());
  darkmode.toggle();
};

var namepreview = document.getElementById("name");

namepreview.onkeyup = namepreview.onkeypress = function () {
  if (this.value) {
    document.getElementById("nameprev").innerHTML = this.value;
  } else {
    document.getElementById("nameprev").innerHTML = "Enter Nft name";
  }
 
};

var floorpreview = document.getElementById("mint_time");

floorpreview.onkeyup = floorpreview.onkeypress = function () {
  if (this.value) {
  document.getElementById("timeprev").innerHTML = this.value;
  } else {
    document.getElementById("timeprev").innerHTML = "  10:80 AM";
  }
};

var datepreview = document.getElementById("date");

datepreview.onkeyup = datepreview.onkeypress = function () {
  if (this.value) {
    document.getElementById("dateprev").innerHTML = this.value;
  } else {
    document.getElementById("dateprev").innerHTML = "Aug 25";
  }
  
};

var totalpreview = document.getElementById("total_supply");

totalpreview.onkeyup = totalpreview.onkeypress = function () {
  if (this.value) {
    document.getElementById("totalprev").innerHTML = this.value +" total";
  } else {
    document.getElementById("totalprev").innerHTML = "1000 total";
  }
  
};

var mintpricepreview = document.getElementById("mint_price");

mintpricepreview.onkeyup = mintpricepreview.onkeypress = function () {
  if (this.value) {
    document.getElementById("mintpreview").innerHTML = this.value;
  } else {
    document.getElementById("mintpreview").innerHTML = "0.77";
  }
  
};

var discord = document.getElementById("discord_url");

discord.onkeyup = discord.onkeypress = function () {
  document.getElementById("disprev").href = this.value;
};

var website = document.getElementById("web_url");

website.onkeyup = website.onkeypress = function () {
  document.getElementById("linkrev").href = this.value;
};

var twitter = document.getElementById("twtr_url");

twitter.onkeyup = twitter.onkeypress = function () {
  document.getElementById("twtprev").href = this.value;
};

var image = document.getElementById("image");

image.onkeyup = image.onkeypress = function () {
  document.getElementById("imageprev").src = this.value;
};

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      $("#imageprev").attr("src", e.target.result).width("100%");
    };
    reader.readAsDataURL(input.files[0]);
  }
}


///////////////////////////////////////////////////////////////////////////////////////////////////////

