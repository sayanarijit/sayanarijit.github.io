// Custom Markdown parser

const markdownIt = require("markdown-it");
const markdownItOptions = {
  html: true,
  linkify: true,
};

const md = new markdownIt(markdownItOptions)
  .use(require("markdown-it-footnote"))
  .use(require("markdown-it-task-lists"))
  .use(require("markdown-it-external-anchor"), { domain: "arijitbasu.in" })
  .use(require("@binyamin/markdown-it-wikilinks"), {
    base: "/notes/",
  })
  .use(require("markdown-it-prism"))
  .use(require("markdown-it-mermaid-plugin"));

// .use(function (md) {
//   // Recognize Mediawiki links ([[text]])
//   md.linkify.add('[[', {
//     validate: /^\s?([^\[\]\|\n\r]+)(\|[^\[\]\|\n\r]+)?\s?\]\]/,
//     normalize: (match) => {
//       const parts = match.raw.slice(2, -2).split('|');
//       parts[0] = parts[0].replace(/.(md|markdown)\s?$/i, '');
//       match.text = (parts[1] || parts[0]).trim();
//       match.url = `/notes/${parts[0].trim()}/`;
//     },
//   });
// });

module.exports = md;
