document.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('toggleSidebar');

  const setCollapsed = (collapsed) => {
    sidebar.dataset.collapsed = collapsed;
    document.cookie = `sidebar_collapsed=${collapsed}; path=/; max-age=31536000`;
    sidebar.style.width = collapsed === "true" ? "4rem" : "16rem";
    document.querySelectorAll('.sidebar-label, .sidebar-title').forEach(el => {
      el.style.display = collapsed === "true" ? "none" : "block";
    });
  };

  // Load initial state
  const cookieMatch = document.cookie.match(/sidebar_collapsed=(true|false)/);
  const initialState = cookieMatch ? cookieMatch[1] : "false";
  setCollapsed(initialState);

  toggleBtn?.addEventListener('click', () => {
    const current = sidebar.dataset.collapsed === "true";
    setCollapsed(current ? "false" : "true");
  });
});
