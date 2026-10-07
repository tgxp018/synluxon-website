(() => {
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
  document.querySelectorAll('[data-language]').forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.language, true)));
  setLanguage(preferred());
})();
