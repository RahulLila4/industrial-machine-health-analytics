-- SELECT COUNT(*) AS total_machines
-- FROM machine_health;

-- SELECT
--     COUNT(*) AS total_machines,
--     SUM(Machine_Failure) AS total_failures,
--     ROUND(
--         SUM(Machine_Failure) * 100.0 / COUNT(*),
--         2
--     ) AS failure_rate_pct
-- FROM machine_health;


-- SELECT
--     Type,
--     COUNT(*) AS total_machines,
--     SUM(Machine_Failure) AS total_failures,
--     ROUND(
--         SUM(Machine_Failure) * 100.0 / COUNT(*),
--         2
--     ) AS failure_rate_pct
-- FROM machine_health
-- GROUP BY Type
-- ORDER BY failure_rate_pct DESC;


-- SELECT 'HDF' AS failure_mode, SUM(HDF) AS occurrences
-- FROM machine_health

-- UNION ALL

-- SELECT 'OSF', SUM(OSF)
-- FROM machine_health

-- UNION ALL

-- SELECT 'PWF', SUM(PWF)
-- FROM machine_health

-- UNION ALL

-- SELECT 'TWF', SUM(TWF)
-- FROM machine_health

-- UNION ALL

-- SELECT 'RNF', SUM(RNF)
-- FROM machine_health

-- ORDER BY occurrences DESC;


-- SELECT
--     Machine_Status,
--     COUNT(*) AS total_machines,
--     ROUND(AVG(Air_Temperature_K), 2) AS avg_air_temp_K,
--     ROUND(AVG(Process_Temperature_K), 2) AS avg_process_temp_K,
--     ROUND(AVG(Rotational_Speed_RPM), 2) AS avg_speed_RPM,
--     ROUND(AVG(Torque_Nm), 2) AS avg_torque_Nm,
--     ROUND(AVG(Tool_Wear_Min), 2) AS avg_tool_wear_min
-- FROM machine_health
-- GROUP BY Machine_Status;


-- SELECT
--     CASE
--         WHEN Torque_Nm < 20 THEN '<20'
--         WHEN Torque_Nm < 30 THEN '20-30'
--         WHEN Torque_Nm < 40 THEN '30-40'
--         WHEN Torque_Nm < 50 THEN '40-50'
--         WHEN Torque_Nm < 60 THEN '50-60'
--         ELSE '>=60'
--     END AS torque_range,

--     COUNT(*) AS total_machines,

--     SUM(Machine_Failure) AS total_failures,

--     ROUND(
--         SUM(Machine_Failure) * 100.0 / COUNT(*),
--         2
--     ) AS failure_rate_pct

-- FROM machine_health

-- GROUP BY torque_range

-- ORDER BY
--     CASE torque_range
--         WHEN '<20' THEN 1
--         WHEN '20-30' THEN 2
--         WHEN '30-40' THEN 3
--         WHEN '40-50' THEN 4
--         WHEN '50-60' THEN 5
--         WHEN '>=60' THEN 6
--     END;


-- SELECT
--     CASE
--         WHEN Tool_Wear_Min < 50 THEN '0-50'
--         WHEN Tool_Wear_Min < 100 THEN '50-100'
--         WHEN Tool_Wear_Min < 150 THEN '100-150'
--         WHEN Tool_Wear_Min < 200 THEN '150-200'
--         WHEN Tool_Wear_Min < 250 THEN '200-250'
--         ELSE '>=250'
--     END AS tool_wear_range,

--     COUNT(*) AS total_machines,

--     SUM(Machine_Failure) AS total_failures,

--     ROUND(
--         SUM(Machine_Failure) * 100.0 / COUNT(*),
--         2
--     ) AS failure_rate_pct

-- FROM machine_health

-- GROUP BY tool_wear_range

-- ORDER BY
--     CASE tool_wear_range
--         WHEN '0-50' THEN 1
--         WHEN '50-100' THEN 2
--         WHEN '100-150' THEN 3
--         WHEN '150-200' THEN 4
--         WHEN '200-250' THEN 5
--         WHEN '>=250' THEN 6
--     END;


SELECT
    CASE
        WHEN Rotational_Speed_RPM < 1300 THEN '<1300'
        WHEN Rotational_Speed_RPM < 1500 THEN '1300-1500'
        WHEN Rotational_Speed_RPM < 1700 THEN '1500-1700'
        WHEN Rotational_Speed_RPM < 1900 THEN '1700-1900'
        WHEN Rotational_Speed_RPM < 2200 THEN '1900-2200'
        ELSE '>=2200'
    END AS speed_range,

    COUNT(*) AS total_machines,

    SUM(Machine_Failure) AS total_failures,

    ROUND(
        SUM(Machine_Failure) * 100.0 / COUNT(*),
        2
    ) AS failure_rate_pct

FROM machine_health

GROUP BY speed_range

ORDER BY
    CASE speed_range
        WHEN '<1300' THEN 1
        WHEN '1300-1500' THEN 2
        WHEN '1500-1700' THEN 3
        WHEN '1700-1900' THEN 4
        WHEN '1900-2200' THEN 5
        WHEN '>=2200' THEN 6
    END;