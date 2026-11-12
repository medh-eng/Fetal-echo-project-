# Prompt 2: Cross-check claims against the source

Use a different model from the one that harvested. Attach the same PDF and paste the claims.

---
You are auditing extracted claims against the attached source document. Do not rely on memory or on the extractor's wording.

For each claim, find the passage at or near the locator and return one verdict:

- CONFIRMED: the document says this, with this strength, at this place.
- CORRECT LOCATOR: true, but found elsewhere (give the right locator).
- DISTORTED: the document says something different (say what, with locator).
- NOT FOUND: you cannot find support in the document.

Then list up to ten important facts in the document, relevant to the unit, that the extractor missed.

Output a table: claim id | verdict | corrected locator or explanation.
Do not rewrite the claims yourself.
