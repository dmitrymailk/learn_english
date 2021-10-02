console.log("start background");

chrome.contextMenus.create({
  contexts: ["all"],
  onclick: (info, tab) => {
    console.log("Context menu", info, tab);
    console.log(info.selectionText);

    let text = info.selectionText;

    chrome.storage.local.set({ selectedText: text });
  },
  title: "My extension",
});
