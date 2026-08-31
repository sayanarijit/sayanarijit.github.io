/**
 * Markdown-it plugin for wikilinks ([[target|label]]) compatible with linkify-it v5+
 */
function wikilinksPlugin(md, opts = {}) {
  const base = opts.base || '/notes/';
  const regex =
    /^([\p{Emoji_Modifier_Base}\p{Emoji_Modifier}?|\p{Emoji_Presentation}|\p{Emoji}\uFE0F\w\s/.-]+?)(?:\s*\|\s*([^\[\]\r\n]+))?\]\]/u;

  md.linkify.add('[[', {
    validate: (text, pos, self) => {
      const tail = text.slice(pos);
      const match = tail.match(regex);
      return match ? match[0].length : 0;
    },
    normalize: (match) => {
      const parts = match.raw.slice(2, -2).split('|');
      const target = parts[0].trim().replace(/\.(md|markdown)$/i, '');
      match.text = (parts[1] || parts[0]).trim();
      match.url = base + target;
    },
  });
}

module.exports = wikilinksPlugin;
