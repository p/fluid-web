/**
host: github.com
*/

window.bsdpower.ready(function() {
  $('.numbers-summary').each(function() {
    var url = $('.numbers-summary li:first-child a').attr('href');
    
    var issuesurl = url.replace(/\/commits\/.*/, '/issues');
    var li = $('<li><a href="">Issues</a></li>');
    li.find('a').attr('href', issuesurl);
    li.insertAfter($('.numbers-summary li:first-child'));
    
    var pullsurl = url.replace(/\/commits\/.*/, '/pulls');
    var li = $('<li><a href="">Pull requests</a></li>');
    li.find('a').attr('href', pullsurl);
    li.insertAfter($('.numbers-summary li:first-child'));
  });
  
  $('.tooltipped').each(function() {
    var e = $(this);
    e.attr('original-title', '');
  });
  
  $('*[data-pjax=true]').each(function() {
    var e = $(this);
    e.attr('data-pjax', '');
  });
  
  /* un-js links */
  
  $('a.js-repo-home-link').each(function() {
    var e = $(this);
    e.removeClass('js-repo-home-link');
  });
  
  /* navigation within pull request (next 2 blocks) */
  
  $('ul.js-hard-tabs').each(function() {
    var e = $(this);
    e.removeClass('js-hard-tabs');
  });
  
  $('a[data-container-id]').each(function() {
    var e = $(this);
    e.removeAttr('data-container-id');
    /* files changed tab gets unnavigable to */
    //var clone = e.clone();
    //clone.insertAfter(e);
    //e[0].parentNode.removeChild(e[0]);
  });
});
