## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/parnaljoshi/COMS574_HW01/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
---
title: | 
         CS 474/574 Machine Learning \
         HW1
author: |
          Parnal Joshi \
          Bioinformatics and Computational Biology PhD Program \
          Veterinary Microbiology and Preventive Medicine \
          Iowa State University \
          Ames, IA, USA \
date:   \today
header-includes: |
     \usepackage{amssymb}
     \usefonttheme[onlymath]{serif}
---

# Warm Up

- \textbf{Newton's First Law of Motion:} Newton's first law states that every object will remain at rest or in uniform motion in a straight line unless acted upon by an external unbalanced force. \
- \textbf{Einstein's Mass-Energy Equation:} $E = mc^2$ \
- \textbf{Time complexity of Quicksort on average in Big-O notation:} $O(nlogn)$ \

# 

The three types of machine learning are:

- Supervised
- Unsupervised
- Reinforcement

# 

The minimum dimension of the vector is $1*5$ (one row five columns)


# Link to github.io

```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

<div id="warm-up" class="slide section level1">
<h1>Warm Up</h1>
<ul>
<li> Newton’s first law states that every object will remain at rest or in uniform motion in a straight line unless acted upon by an external unbalanced force.<br />
</li>
<li> <span class="math inline"><em>E</em> = <em>m</em><em>c</em><sup>2</sup></span><br />
</li>
<li> <span class="math inline"><em>O</em>(<em>n</em><em>l</em><em>o</em><em>g</em><em>n</em>)</span><br />
</li>
</ul>
</div>
<div id="section" class="slide section level1">
<h1></h1>
<p>The three types of machine learning are:</p>
<ul>
<li>Supervised</li>
<li>Unsupervised</li>
<li>Reinforcement</li>
</ul>
</div>
<div id="section-1" class="slide section level1">
<h1></h1>
<p>The minimum dimension of the vector is <span class="math inline">1 * 5</span> (one row five columns)</p>
</div>
<div id="section-2" class="slide section level1">
<h1></h1>
<p></p>
</div>


### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/parnaljoshi/COMS574_HW01/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.

### Trial

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box}
body {font-family: Verdana, sans-serif; margin:0}
.mySlides {display: none}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .prev, .next,.text {font-size: 11px}
}
</style>
</head>
<body>

<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <div class="text">Caption Text</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <div class="text">Caption Two</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <div class="text">Caption Three</div>
</div>

<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
<a class="next" onclick="plusSlides(1)">&#10095;</a>

</div>
<br>

<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span> 
  <span class="dot" onclick="currentSlide(2)"></span> 
  <span class="dot" onclick="currentSlide(3)"></span> 
</div>

<script>
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}
</script>

</body>
</html> 
