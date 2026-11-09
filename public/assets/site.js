(() => {
  const root = document.documentElement;
  const themeKey = 'synluxon-theme';
  const themeColor = document.querySelector('meta[name="theme-color"]');
  const setTheme = theme => {
    root.dataset.theme = theme;
    themeColor.content = theme === 'light' ? '#f7f8f4' : '#111315';
  };
  let initialTheme = 'dark';
  try { if (localStorage.getItem(themeKey) === 'light') initialTheme = 'light'; } catch (_) {}
  setTheme(initialTheme);

  const storageKey = 'synluxon-language';
  const preferred = () => {
    try { const saved = localStorage.getItem(storageKey); if (saved === 'en' || saved === 'zh') return saved; } catch (_) {}
    return (navigator.languages || [navigator.language]).some(lang => /^zh\b/i.test(lang)) ? 'zh' : 'en';
  };
  const setLanguage = (language, persist = false) => {
    const lang = language === 'zh' ? 'zh' : 'en';
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('[data-en][data-zh]').forEach(node => { node.textContent = node.dataset[lang]; });
    document.querySelectorAll('[data-en-content]').forEach(node => { node.content = node.dataset[`${lang}Content`]; });
    document.querySelectorAll('[data-en-aria]').forEach(node => { node.setAttribute('aria-label', node.dataset[`${lang}Aria`]); });
    document.querySelectorAll('[data-language]').forEach(button => { button.setAttribute('aria-pressed', String(button.dataset.language === lang)); });
    if (persist) { try { localStorage.setItem(storageKey, lang); } catch (_) {} }
  };
  document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('[data-theme-toggle]');
    toggle.setAttribute('aria-pressed', String(root.dataset.theme === 'dark'));
    toggle.addEventListener('click', () => {
      const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      setTheme(theme);
      toggle.setAttribute('aria-pressed', String(theme === 'dark'));
      try { localStorage.setItem(themeKey, theme); } catch (_) {}
    });
    toggle.hidden = false;
    document.querySelectorAll('[data-language]').forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.language, true)));
    setLanguage(preferred());
  });
})();
