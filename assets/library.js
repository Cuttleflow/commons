/* Renders "the rest of the library" on each wording page.
   Cards show a neutral "Open to comment" state. Comments live in GitHub Discussions
   (giscus), which has no public per-page count API, so no count is claimed here —
   better silent than a false "no comments yet".                                     */
var COMMONS_WORDINGS = [
  {slug:"professional-indemnity",       cls:"Professional Indemnity", t:"Professional Indemnity"},
  {slug:"directors-and-officers",       cls:"Directors & Officers",   t:"Directors & Officers"},
  {slug:"side-a-do",                    cls:"Side A D&O",             t:"Side A D&O"},
  {slug:"management-liability",         cls:"Management Liability",    t:"Management Liability"},
  {slug:"investment-management-insurance",cls:"Investment Management", t:"Investment Managers Indemnity"},
  {slug:"cyber",                        cls:"Cyber",                  t:"Cyber"},
  {slug:"crime",                        cls:"Crime",                  t:"Comprehensive Crime"},
  {slug:"technology-liability",         cls:"Technology Liability",   t:"Technology Liability"}
];
(function(){
  var box=document.getElementById("more-wordings"); if(!box) return;
  var here=(location.pathname.split("/").pop()||"").replace(".html","");
  var others=COMMONS_WORDINGS.filter(function(w){return w.slug!==here;});
  var urls={};
  others.forEach(function(w){
    var u=new URL(w.slug+".html", location.href).href; urls[u]=w;
    var a=document.createElement("a"); a.className="more-card"; a.href=w.slug+".html"; a.dataset.url=u;
    a.innerHTML='<span class="cls">'+w.cls+'</span><span class="t">'+w.t+'</span>'+
                '<span class="st" data-role="st">Open to comment &rarr;</span>';
    box.appendChild(a);
  });
})();
