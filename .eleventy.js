module.exports = function (eleventyConfig) {
  const md = require("./eleventy/markdownIt");
  eleventyConfig.setLibrary("md", md);

  // filters
  require("./eleventy/filters")(eleventyConfig, md);

  // Shortcodes
  require("./eleventy/shortcodes")(eleventyConfig, md);

  const wm = require("./eleventy/webmentions");
  eleventyConfig.addFilter("getMentionsForUrl", wm);

  eleventyConfig.addCollection("notes", function (collection) {
    return collection.getFilteredByGlob(["src/site/notes/*.md"]);
  });

  eleventyConfig.addCollection("posts", function (collection) {
    return collection
      .getFilteredByGlob(["src/site/blog/*.md"])
      .filter((item) => !item.inputPath.endsWith("index.md"))
      .sort((a, b) => b.data.index - a.data.index);
  });

  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  eleventyConfig.addPassthroughCopy({ "src/site/keybase.txt": "keybase.txt" });
  eleventyConfig.addPassthroughCopy({ "src/site/gpg.txt": "gpg.txt" });
  eleventyConfig.addPassthroughCopy({ "src/site/id_rsa.txt": "id_rsa.txt" });
  eleventyConfig.addPassthroughCopy({
    "src/site/id_ed25519.txt": "id_ed25519.txt",
  });
  eleventyConfig.addPassthroughCopy({
    "src/site/keyboard.html": "keyboard.html",
  });
  eleventyConfig.setUseGitIgnore(false);

  const embedYouTube = require("eleventy-plugin-youtube-embed");
  eleventyConfig.addPlugin(embedYouTube, { lite: true });

  const pluginRss = require("@11ty/eleventy-plugin-rss");
  eleventyConfig.addPlugin(pluginRss);

  return {
    dir: {
      input: "./src/site",
      output: "dist",
      layouts: "../layouts",
      includes: "../includes",
      data: "../data",
    },
    passthroughFileCopy: true,
  };
};
