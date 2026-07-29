/* Cuttleflow Commons — comment layer (giscus, backed by GitHub Discussions).

   One sign-in path, by design: a GitHub account. Anyone who does not have one — or
   does not want one — uses the issue form instead ("Suggest a change" / the form
   link in the sign-in note). Both routes land in the same repository.

   Comments live in GitHub Discussions on cuttleflow/commons. There is no server
   to run and nothing to host: if the repo is public, this works.

   SETUP: install the giscus app on the repo and enable Discussions, then paste the
   two ids below from https://giscus.app (it reads them off your repo for you).
   Until they are filled in, the comment area stays empty and nothing errors.      */

window.GISCUS_REPO    = "cuttleflow/commons";
window.GISCUS_REPO_ID = "";   // <-- from giscus.app
window.GISCUS_CAT_ID  = "";   // <-- from giscus.app (use the "Wordings" category)

(function () {
  var mount = document.querySelector(".giscus");
  if (!mount) return;

  if (!window.GISCUS_REPO_ID || !window.GISCUS_CAT_ID) {
    console.info("[commons] giscus not configured yet — see assets/comments.js");
    return;
  }

  var s = document.createElement("script");
  s.src = "https://giscus.app/client.js";
  s.async = true;
  s.crossOrigin = "anonymous";
  s.setAttribute("data-repo", window.GISCUS_REPO);
  s.setAttribute("data-repo-id", window.GISCUS_REPO_ID);
  s.setAttribute("data-category-id", window.GISCUS_CAT_ID);
  s.setAttribute("data-mapping", "pathname");
  s.setAttribute("data-strict", "1");
  s.setAttribute("data-reactions-enabled", "1");
  s.setAttribute("data-emit-metadata", "0");
  s.setAttribute("data-input-position", "top");
  s.setAttribute("data-theme", "light");
  s.setAttribute("data-lang", "en");
  s.setAttribute("data-loading", "lazy");
  mount.appendChild(s);
})();
