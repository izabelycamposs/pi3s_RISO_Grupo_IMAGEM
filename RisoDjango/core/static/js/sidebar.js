document.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('toggleSidebar');
  const labels = document.querySelectorAll('.sidebar-label');
  const title = document.getElementById('sidebar-title');

  const setCollapsed = (collapsed) => {
    const isCollapsed = collapsed === 'true';

    // Salvar em cookie
    document.cookie = `sidebar_collapsed=${collapsed}; path=/; max-age=31536000`;

    // Aplicar largura
    sidebar.style.width = isCollapsed ? '5.5rem' : '16rem';

    // Mostrar/ocultar textos
    labels.forEach(label => {
      label.classList.toggle('hidden', isCollapsed);
    });

    if (title) {
      title.classList.toggle('hidden', isCollapsed);
    }

    sidebar.dataset.collapsed = collapsed;
  };

  // Pega o estado salvo no cookie
  const getCookie = (name) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    return parts.length === 2 ? parts.pop().split(';').shift() : null;
  };

  const initial = getCookie('sidebar_collapsed') || 'false';
  setCollapsed(initial);

  toggleBtn?.addEventListener('click', () => {
    const isCollapsed = sidebar.dataset.collapsed === 'true';
    setCollapsed(!isCollapsed + '');
  });
});
