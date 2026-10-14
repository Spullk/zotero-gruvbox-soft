/* Gruvbox Soft — injects style.css into every Zotero main window. */

var rootURI;
const STYLE_ID = "gruvbox-soft-stylesheet";

function addStyle(window) {
  const doc = window.document;
  if (doc.getElementById(STYLE_ID)) return;
  const link = doc.createElement("link");
  link.id = STYLE_ID;
  link.type = "text/css";
  link.rel = "stylesheet";
  link.href = rootURI + "style.css";
  doc.documentElement.appendChild(link);
}

function removeStyle(window) {
  const link = window.document.getElementById(STYLE_ID);
  if (link) link.remove();
}

function install() {}
function uninstall() {}

async function startup({ id, version, rootURI: uri }) {
  rootURI = uri;
  // Theme any windows that are already open (e.g. plugin enabled mid-session)
  for (const win of Zotero.getMainWindows()) {
    addStyle(win);
  }
}

function onMainWindowLoad({ window }) {
  addStyle(window);
}

function onMainWindowUnload({ window }) {
  removeStyle(window);
}

function shutdown() {
  for (const win of Zotero.getMainWindows()) {
    removeStyle(win);
  }
}
