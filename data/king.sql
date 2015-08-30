INSERT INTO king_soldier_skill_conj (
	skill_id,
	soldier_id,
	skill_level
) SELECT
	j.id,
	b.id,
	0
FROM
	king_soldier b
JOIN king_soldier_skills j ON b.skill_green = j.id;

INSERT INTO king_soldier_skill_conj (
	skill_id,
	soldier_id,
	skill_level
) SELECT
	j.id,
	b.id,
	1
FROM
	king_soldier b
JOIN king_soldier_skills j ON b.skill_blue = j.id;

INSERT INTO king_soldier_skill_conj (
	skill_id,
	soldier_id,
	skill_level
) SELECT
	j.id,
	b.id,
	2
FROM
	king_soldier b
JOIN king_soldier_skills j ON b.skill_purple = j.id;

INSERT INTO king_soldier_skill_conj (
	skill_id,
	soldier_id,
	skill_level
) SELECT
	j.id,
	b.id,
	3
FROM
	king_soldier b
JOIN king_soldier_skills j ON b.skill_gold = j.id;


SELECT sk.* FROM king_soldier_skills sk JOIN king_soldier_skill_conj con on sk.id = con.skill_id WHERE con.soldier_id = 6 ORDER BY con.skill_level;