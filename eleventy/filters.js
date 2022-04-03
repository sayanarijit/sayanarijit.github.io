const { titleCase } = require('title-case');

module.exports = (eleventyConfig, md) => {
  eleventyConfig.addFilter('absolute_url', (slug) => {
    return (
      'https://ariijitbasu.in' + (slug.startsWith('/') ? slug : '/' + slug)
    );
  });

  eleventyConfig.addFilter('edit_note', (slug) => {
    slug = slug.endsWith('/') ? slug.slice(0, -1) : slug;
    slug = slug.startsWith('/') ? slug : '/' + slug;
    return `https://github.com/sayanarijit/sayanarijit.github.io/edit/main/src/site${slug}.md`;
  });

  const filters = {
    ...require('./date_filter'),
    ...require('./sort_ab_filter'),
  };

  for (const fn in filters) {
    eleventyConfig.addFilter(fn, filters[fn]);
  }

  eleventyConfig.addFilter('escape_once', (str) => {
    // From <https://github.com/harttle/liquidjs/blob/master/src/builtin/filters/html.ts>
    const escapeMap = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&#34;',
      "'": '&#39;',
    };
    const unescapeMap = {
      '&amp;': '&',
      '&lt;': '<',
      '&gt;': '>',
      '&#34;': '"',
      '&#39;': "'",
    };

    function escape(str) {
      return String(str).replace(/&|<|>|"|'/g, (m) => escapeMap[m]);
    }

    function unescape(str) {
      return String(str).replace(
        /&(amp|lt|gt|#34|#39);/g,
        (m) => unescapeMap[m]
      );
    }

    return escape(unescape(str));
  });

  eleventyConfig.addFilter('titlecase', (str) => {
    return titleCase(str);
  });

  eleventyConfig.addFilter('includes', (arr, value) => {
    return arr.includes(value);
  });

  eleventyConfig.addFilter('slugify', (str) => {
    return str
      .toLowerCase()
      .replace(/[^\w\s-]+/g, '')
      .replace(/\s+/g, '-');
  });

  eleventyConfig.addFilter('markdownify', (string) => {
    return md.renderInline(string);
  });

  function filterTagList(tags) {
    return (tags || []).filter(
      (tag) =>
        ['all', 'nav', 'post', 'posts', 'note', 'notes'].indexOf(tag) === -1
    );
  }

  eleventyConfig.addFilter('filterTagList', filterTagList);

  // Create an array of all tags
  eleventyConfig.addCollection('tagList', function (collection) {
    let tagSet = new Set();
    collection.getAll().forEach((item) => {
      (item.data.tags || []).forEach((tag) => tagSet.add(tag));
    });

    let tags = filterTagList([...tagSet]);
    tags.sort();
    return tags;
  });
};
