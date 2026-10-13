(() => {
  const indexUrl = document.currentScript.dataset.index;
  const input = document.getElementById('search-input');
  const results = document.getElementById('results-container');
  const status = document.getElementById('search-status');
  let posts = [];
  let ready = false;

  function render() {
    results.replaceChildren();
    const query = input.value.trim().toLocaleLowerCase();
    if (!ready || !query) {
      status.textContent = query ? 'Loading posts…' : '';
      return;
    }
    const matches = posts.filter(post =>
      `${post.title} ${post.category}`.toLocaleLowerCase().includes(query)
    );
    status.textContent = matches.length
      ? `${matches.length} ${matches.length === 1 ? 'post' : 'posts'} found.`
      : 'No posts found. Try another title or topic.';
    for (const post of matches) {
      const item = document.createElement('li');
      const heading = document.createElement('h2');
      const link = document.createElement('a');
      link.href = post.url;
      link.textContent = post.title;
      heading.append(link);
      const date = document.createElement('p');
      date.textContent = post.date;
      item.append(heading, date);
      results.append(item);
    }
  }

  input.addEventListener('input', render);
  fetch(indexUrl)
    .then(response => {
      if (!response.ok) throw new Error('Search index unavailable');
      return response.json();
    })
    .then(data => {
      posts = data;
      ready = true;
      render();
    })
    .catch(() => {
      status.textContent = 'Search is unavailable. Please use the post archive.';
      input.disabled = true;
    });
})();
