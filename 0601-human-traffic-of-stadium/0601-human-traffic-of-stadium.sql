SELECT DISTINCT s.*
FROM Stadium s
JOIN Stadium s1 ON s1.id = s.id - 1
JOIN Stadium s2 ON s2.id = s.id - 2
WHERE s.people >= 100
  AND s1.people >= 100
  AND s2.people >= 100

UNION

SELECT DISTINCT s.*
FROM Stadium s
JOIN Stadium s1 ON s1.id = s.id + 1
JOIN Stadium s2 ON s2.id = s.id + 2
WHERE s.people >= 100
  AND s1.people >= 100
  AND s2.people >= 100

UNION

SELECT DISTINCT s.*
FROM Stadium s
JOIN Stadium s1 ON s1.id = s.id - 1
JOIN Stadium s2 ON s2.id = s.id + 1
WHERE s.people >= 100
  AND s1.people >= 100
  AND s2.people >= 100

ORDER BY visit_date;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna