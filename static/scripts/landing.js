window.addEventListener('DOMContentLoaded', () => {
  // Only animate nav and main content, not video
  const navElements = [...document.querySelectorAll('.nav2 > div')].filter(Boolean);
  const mainElements = [
    document.querySelector('.tex'),
    document.querySelector('.subtex'),
    document.querySelector('.exp_butt')
  ].filter(Boolean);

  // Sequentially show nav bar elements faster
  function showNavSequentially(index = 0) {
    if (index < navElements.length) {
      const el = navElements[index];
      el.classList.remove('hidden');
      el.classList.add('fade-in');
      setTimeout(() => showNavSequentially(index + 1), 150); // Faster speed
    }
  }

  // Sequentially show main elements
  function showMainSequentially(index = 0) {
    if (index < mainElements.length) {
      const el = mainElements[index];
      el.classList.remove('hidden');
      el.classList.add('fade-in');
      setTimeout(() => showMainSequentially(index + 1), 350);
    }
  }

  showNavSequentially();
  setTimeout(() => showMainSequentially(), navElements.length * 150);
});
