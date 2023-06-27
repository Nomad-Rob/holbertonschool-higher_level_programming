-- Displace Scores and how often it happens
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
