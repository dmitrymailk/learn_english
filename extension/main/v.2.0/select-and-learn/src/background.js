console.log("start background");
console.log(chrome.contextMenus);
const createContextMenu = () => {
  chrome.contextMenus.create({
    contexts: ["all"],
    title: "My extension",
    id: "1",
  });
};
createContextMenu();

chrome.contextMenus.onClicked.addListener((info, tab) => {
  console.log("Context menu", info, tab);
  console.log(info.selectionText);

  let text = info.selectionText;

  chrome.storage.local.set({ selectedText: text });
  chrome.contextMenus.removeAll();
  createContextMenu();
});
