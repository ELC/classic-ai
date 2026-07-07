import { readFileSync } from 'node:fs';

const CARD_DATA_URL = new URL('../data/flashcards.json', import.meta.url);
const WIDGET_MODULE = '../../plugins/flashcards-widget.mjs';

/**
 * @typedef {{ title: string; cards: unknown[] }} UnitCardData
 * @typedef {{ source: string; units: Record<string, UnitCardData> }} CardData
 */

/** @type {CardData | undefined} */
let cardData;

/** @returns {CardData} */
function loadCardData() {
  if (cardData) return cardData;
  cardData = /** @type {CardData} */ (JSON.parse(readFileSync(CARD_DATA_URL, 'utf8')));
  return cardData;
}

/** @param {string} unit */
function widgetId(unit) {
  return `flashcards-${unit}-${Math.random().toString(36).slice(2, 10)}`;
}

/** @param {string} unit */
function flashcardsNode(unit) {
  const data = loadCardData();
  const unitData = data.units[unit];
  if (!unitData) {
    throw new Error(`No review flashcards found for unit ${unit}`);
  }
  return [
    {
      type: 'anywidget',
      esm: WIDGET_MODULE,
      model: {
        unit,
        title: unitData.title,
        cards: unitData.cards,
      },
      class: 'flashcards-widget',
      id: widgetId(unit),
    },
  ];
}

/** @param {string} unit */
function unitFlashcardsDirective(unit) {
  return {
    name: `flashcards-${unit}`,
    doc: `Insert the client-side review flashcard widget for unit ${unit}.`,
    arg: {
      type: String,
      doc: 'Ignored compact-directive marker emitted by mdformat.',
    },
    run() {
      return flashcardsNode(unit);
    },
  };
}

const flashcardsDirectives = ['01', '02', '03', '04', '05'].map(unitFlashcardsDirective);

const plugin = {
  name: 'Review Flashcards',
  directives: flashcardsDirectives,
};

export default plugin;
