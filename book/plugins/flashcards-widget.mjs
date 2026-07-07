const STORAGE_VERSION = 1;

/**
 * @typedef {{ label: string; html: string }} FlashcardAnswer
 * @typedef {{ id: string; questionHtml: string; answers: FlashcardAnswer[]; sourceHtml: string }} Flashcard
 * @typedef {{ order: string[]; current: number; revealed: boolean }} FlashcardState
 * @typedef {{ secondary?: boolean }} ButtonOptions
 * @typedef {{ get: (key: string) => unknown }} AnyWidgetModel
 */

/** @returns {string} */
function siteBasePath() {
  const marker = '/chapters/';
  const index = window.location.pathname.indexOf(marker);
  return index === -1 ? '' : window.location.pathname.slice(0, index);
}

/** @param {string} path */
function sitePath(path) {
  return `${siteBasePath()}/${String(path).replace(/^\/+/, '')}`;
}

/** @param {string} unit */
function storageKey(unit) {
  return `classic-ai:flashcards:v${STORAGE_VERSION}:unit-${unit}`;
}

/**
 * @template Value
 * @param {Value[]} values
 * @returns {Value[]}
 */
function shuffled(values) {
  const result = [...values];
  for (let index = result.length - 1; index > 0; index -= 1) {
    const swapIndex = Math.floor(Math.random() * (index + 1));
    [result[index], result[swapIndex]] = [result[swapIndex], result[index]];
  }
  return result;
}

/**
 * @param {string} unit
 * @param {Flashcard[]} cards
 * @returns {FlashcardState}
 */
function loadState(unit, cards) {
  const defaultOrder = cards.map((card) => card.id);
  try {
    const raw = window.localStorage.getItem(storageKey(unit));
    if (!raw) return { order: defaultOrder, current: 0, revealed: false };

    const parsed = JSON.parse(raw);
    const ids = new Set(defaultOrder);
    const order = /** @type {string[]} */ (Array.isArray(parsed.order) ? parsed.order.map(String) : []);
    const orderIsValid = order.length === defaultOrder.length && order.every((id) => ids.has(id));
    if (!orderIsValid) return { order: defaultOrder, current: 0, revealed: false };

    const current = Number.isInteger(parsed.current)
      ? Math.min(Math.max(parsed.current, 0), order.length - 1)
      : 0;
    return { order, current, revealed: Boolean(parsed.revealed) };
  } catch {
    return { order: defaultOrder, current: 0, revealed: false };
  }
}

/**
 * @param {string} unit
 * @param {FlashcardState} state
 */
function saveState(unit, state) {
  try {
    window.localStorage.setItem(storageKey(unit), JSON.stringify(state));
  } catch {
    // Private browsing or storage limits should not break studying.
  }
}

/** @param {ParentNode} root */
function normalizeDynamicLinks(root) {
  for (const link of root.querySelectorAll('[data-book-path]')) {
    if (link instanceof HTMLAnchorElement && link.dataset.bookPath) {
      link.setAttribute('href', sitePath(link.dataset.bookPath));
    }
  }
  for (const image of root.querySelectorAll('[data-flashcard-media]')) {
    if (image instanceof HTMLImageElement && image.dataset.flashcardMedia) {
      image.setAttribute('src', sitePath(`assets/flashcards/${image.dataset.flashcardMedia}`));
    }
  }
}

/**
 * @param {HTMLElement} element
 * @param {string} html
 */
function setHtml(element, html) {
  element.innerHTML = html;
  normalizeDynamicLinks(element);
}

/**
 * @param {string} label
 * @param {EventListener} onClick
 * @param {ButtonOptions} [options]
 */
function createButton(label, onClick, options = {}) {
  const button = document.createElement('button');
  button.type = 'button';
  button.className = options.secondary ? 'flashcards-button flashcards-button-secondary' : 'flashcards-button';
  button.textContent = label;
  button.addEventListener('click', onClick);
  return button;
}

/**
 * @param {Flashcard[]} cards
 * @returns {Map<string, Flashcard>}
 */
function cardById(cards) {
  return new Map(cards.map((card) => [card.id, card]));
}

/** @param {{ model: AnyWidgetModel; el: HTMLElement }} ctx */
function render({ model, el }) {
  const unit = String(model.get('unit') ?? '');
  const title = String(model.get('title') ?? `Unidad ${unit}`);
  const rawCards = model.get('cards');
  const cards = Array.isArray(rawCards) ? /** @type {Flashcard[]} */ (rawCards) : [];
  const cardsById = cardById(cards);
  const defaultOrder = cards.map((card) => card.id);
  let state = loadState(unit, cards);

  const root = document.createElement('section');
  root.className = 'flashcards';
  root.tabIndex = 0;
  root.setAttribute('aria-label', `Tarjetas de repaso de ${title}`);

  const style = document.createElement('style');
  style.textContent = `
    .flashcards {
      --flashcards-surface: #ffffff;
      --flashcards-card-surface: #f8fafc;
      --flashcards-text: #111827;
      --flashcards-muted-text: #475569;
      --flashcards-border: #cbd5e1;
      --flashcards-primary: #2563eb;
      --flashcards-primary-hover: #1d4ed8;
      --flashcards-primary-text: #ffffff;
      --flashcards-secondary-surface: #eef2ff;
      --flashcards-secondary-hover: #e0e7ff;
      --flashcards-secondary-border: #6366f1;
      --flashcards-secondary-text: #312e81;
      --flashcards-link: #1d4ed8;
      --flashcards-link-hover: #1e40af;
      --flashcards-focus: #2563eb;

      border: 1px solid var(--flashcards-border);
      border-radius: 0.9rem;
      padding: 1rem;
      margin-block: 1.5rem;
      background: var(--flashcards-surface);
      color: var(--flashcards-text);
      box-shadow: 0 1rem 2.5rem rgb(15 23 42 / 0.08);
    }

    @media (prefers-color-scheme: dark) {
      .flashcards {
        --flashcards-surface: #111827;
        --flashcards-card-surface: #1f2937;
        --flashcards-text: #f8fafc;
        --flashcards-muted-text: #cbd5e1;
        --flashcards-border: #475569;
        --flashcards-primary: #60a5fa;
        --flashcards-primary-hover: #93c5fd;
        --flashcards-primary-text: #0f172a;
        --flashcards-secondary-surface: #172554;
        --flashcards-secondary-hover: #1e3a8a;
        --flashcards-secondary-border: #60a5fa;
        --flashcards-secondary-text: #dbeafe;
        --flashcards-link: #93c5fd;
        --flashcards-link-hover: #bfdbfe;
        --flashcards-focus: #93c5fd;
        box-shadow: 0 1rem 2.5rem rgb(0 0 0 / 0.32);
      }
    }

    .flashcards:focus-visible {
      outline: 3px solid var(--flashcards-focus);
      outline-offset: 4px;
    }

    .flashcards-header,
    .flashcards-controls {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      align-items: center;
      justify-content: space-between;
    }

    .flashcards-title {
      margin: 0;
      font-size: 1rem;
      font-weight: 700;
    }

    .flashcards-progress,
    .flashcards-shortcuts {
      margin: 0;
      font-size: 0.9rem;
      color: var(--flashcards-muted-text);
    }

    .flashcards-shortcuts {
      margin-top: 0.75rem;
    }

    .flashcards-card {
      border: 1px solid var(--flashcards-border);
      border-radius: 0.75rem;
      padding: 1rem;
      margin-block: 1rem;
      background: var(--flashcards-card-surface);
    }

    .flashcards-question {
      font-size: 1.08rem;
      line-height: 1.55;
    }

    .flashcards-answer {
      display: grid;
      gap: 0.85rem;
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 1px solid var(--flashcards-border);
    }

    .flashcards-answer-section h3,
    .flashcards-source h3 {
      margin: 0 0 0.25rem;
      font-size: 0.95rem;
    }

    .flashcards-answer-section div,
    .flashcards-source div {
      line-height: 1.55;
    }

    .flashcards a {
      color: var(--flashcards-link);
      font-weight: 600;
      text-decoration-thickness: 0.12em;
      text-underline-offset: 0.18em;
    }

    .flashcards a:hover {
      color: var(--flashcards-link-hover);
    }

    .flashcards a:focus-visible {
      outline: 2px solid var(--flashcards-focus);
      outline-offset: 3px;
      border-radius: 0.2rem;
    }

    .flashcards img {
      max-width: min(100%, 44rem);
      height: auto;
      display: block;
      margin-block: 0.75rem;
      border-radius: 0.5rem;
    }

    .flashcards-button-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .flashcards-button {
      border: 1px solid var(--flashcards-primary);
      border-radius: 999px;
      padding: 0.45rem 0.85rem;
      font: inherit;
      font-weight: 600;
      color: var(--flashcards-primary-text);
      background: var(--flashcards-primary);
      cursor: pointer;
      box-shadow: 0 0.45rem 1rem rgb(37 99 235 / 0.22);
    }

    .flashcards-button:hover:not(:disabled) {
      border-color: var(--flashcards-primary-hover);
      background: var(--flashcards-primary-hover);
    }

    .flashcards-button:focus-visible {
      outline: 2px solid var(--flashcards-focus);
      outline-offset: 2px;
    }

    .flashcards-button:disabled {
      cursor: not-allowed;
      opacity: 0.58;
      box-shadow: none;
    }

    .flashcards-button-secondary {
      border-color: var(--flashcards-secondary-border);
      color: var(--flashcards-secondary-text);
      background: var(--flashcards-secondary-surface);
      box-shadow: none;
    }

    .flashcards-button-secondary:hover:not(:disabled) {
      border-color: var(--flashcards-secondary-border);
      color: var(--flashcards-secondary-text);
      background: var(--flashcards-secondary-hover);
    }

    @media (max-width: 42rem) {
      .flashcards {
        padding: 0.85rem;
      }

      .flashcards-header,
      .flashcards-controls {
        align-items: stretch;
      }

      .flashcards-button-row,
      .flashcards-button {
        width: 100%;
      }
    }
  `;

  function currentCard() {
    return cardsById.get(state.order[state.current]) ?? cards[0];
  }

  function persistAndRender() {
    saveState(unit, state);
    draw();
  }

  function reveal() {
    state = { ...state, revealed: true };
    persistAndRender();
  }

  function previous() {
    state = { ...state, current: Math.max(0, state.current - 1), revealed: false };
    persistAndRender();
  }

  function next() {
    state = {
      ...state,
      current: Math.min(state.order.length - 1, state.current + 1),
      revealed: false,
    };
    persistAndRender();
  }

  function shuffleCards() {
    state = { order: shuffled(defaultOrder), current: 0, revealed: false };
    persistAndRender();
  }

  function reset() {
    state = { order: defaultOrder, current: 0, revealed: false };
    persistAndRender();
  }

  function draw() {
    const card = currentCard();
    root.replaceChildren();
    root.append(style);

    const header = document.createElement('div');
    header.className = 'flashcards-header';

    const heading = document.createElement('h2');
    heading.className = 'flashcards-title';
    heading.textContent = title;

    const progress = document.createElement('p');
    progress.className = 'flashcards-progress';
    progress.textContent = `Tarjeta ${state.current + 1} de ${cards.length}`;

    header.append(heading, progress);

    const cardContainer = document.createElement('article');
    cardContainer.className = 'flashcards-card';

    const question = document.createElement('div');
    question.className = 'flashcards-question';
    setHtml(question, card.questionHtml);
    cardContainer.append(question);

    if (state.revealed) {
      const answer = document.createElement('div');
      answer.className = 'flashcards-answer';

      for (const answerPart of card.answers) {
        const section = document.createElement('section');
        section.className = 'flashcards-answer-section';

        const sectionHeading = document.createElement('h3');
        sectionHeading.textContent = answerPart.label;

        const sectionBody = document.createElement('div');
        setHtml(sectionBody, answerPart.html);

        section.append(sectionHeading, sectionBody);
        answer.append(section);
      }

      const source = document.createElement('section');
      source.className = 'flashcards-source';
      const sourceHeading = document.createElement('h3');
      sourceHeading.textContent = 'Fuente';
      const sourceBody = document.createElement('div');
      setHtml(sourceBody, card.sourceHtml);
      source.append(sourceHeading, sourceBody);
      answer.append(source);

      cardContainer.append(answer);
    }

    const controls = document.createElement('div');
    controls.className = 'flashcards-controls';

    const mainButtons = document.createElement('div');
    mainButtons.className = 'flashcards-button-row';
    const previousButton = createButton('Anterior', previous, { secondary: true });
    previousButton.disabled = state.current === 0;
    const revealButton = createButton('Revelar', reveal);
    revealButton.disabled = state.revealed;
    const nextButton = createButton('Siguiente', next, { secondary: true });
    nextButton.disabled = state.current === cards.length - 1;
    mainButtons.append(previousButton, revealButton, nextButton);

    const sessionButtons = document.createElement('div');
    sessionButtons.className = 'flashcards-button-row';
    sessionButtons.append(
      createButton('Mezclar', shuffleCards, { secondary: true }),
      createButton('Reiniciar', reset, { secondary: true }),
    );

    controls.append(mainButtons, sessionButtons);

    const shortcuts = document.createElement('p');
    shortcuts.className = 'flashcards-shortcuts';
    shortcuts.textContent = 'Atajos: Espacio revela, flechas navegan.';

    root.append(header, cardContainer, controls, shortcuts);
  }

  /** @param {KeyboardEvent} event */
  function onKeyDown(event) {
    if (event.key === ' ') {
      event.preventDefault();
      if (!state.revealed) reveal();
    } else if (event.key === 'ArrowLeft' && state.current > 0) {
      event.preventDefault();
      previous();
    } else if (event.key === 'ArrowRight' && state.current < cards.length - 1) {
      event.preventDefault();
      next();
    }
  }

  root.addEventListener('keydown', onKeyDown);
  el.append(root);
  draw();

  return () => {
    root.removeEventListener('keydown', onKeyDown);
    root.remove();
  };
}

export default { render };
