const { titleCase } = require("title-case");

module.exports = {
  layout: "post.html",
  type: "post",
  tags: ["posts"],
  eleventyComputed: {
    title: (data) => data.title || titleCase(data.page.fileSlug),
  },
};
