from dateutil.relativedelta import relativedelta
from log.models import Log

from psqlextra.partitioning import (
    PostgresPartitioningManager,
    PostgresCurrentTimePartitioningStrategy,
    PostgresTimePartitionSize,
    partition_by_current_time,
)
from psqlextra.partitioning.config import PostgresPartitioningConfig

manager = PostgresPartitioningManager(
    [
        # 3 partitions ahead, each partition is one month
        # delete partitions older than 6 months
        # partitions will be named `[table_name]_[year]_[3-letter month name]`.
        PostgresPartitioningConfig(
            model=Log,
            strategy=PostgresCurrentTimePartitioningStrategy(
                size=PostgresTimePartitionSize(months=1),
                count=3,
            ),
        ),
    ]
)
