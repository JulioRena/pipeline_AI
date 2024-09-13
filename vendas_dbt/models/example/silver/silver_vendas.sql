{{ config(materialized='view') }}


WITH cleaned_data AS(
    select
    email,
    DATE(data) as data,
    valor,
    quantidade,
    produto
    from
    {{ ref('bronze_vendas') }}
    WHERE
        valor between 1 AND 9000
        and data >= '2024-09-01'
        and data <= '2024-12-11'
)

SELECT * FROM cleaned_data