with test_cte as (
    select row_number() over (partition by PlaylistId order by Name) as pos
    from playlists
)

select
    'fail' AS test
from test_cte

where not(pos = 1)