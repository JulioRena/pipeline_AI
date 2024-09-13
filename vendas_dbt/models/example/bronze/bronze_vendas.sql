{{ config(materialized='view') }}

select
    *
from
{{ source('vendas_source', 'vendas') }}