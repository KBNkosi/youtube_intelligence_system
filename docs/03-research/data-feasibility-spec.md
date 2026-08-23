Objective:
Determine whether retention and transcript data can be aligned.

Inputs:
Authorised YouTube video.

Required data:
- Video duration
- Transcript timestamps
- Retention timeline

Expected behaviour:
Retention positions can be mapped to video seconds
and associated with transcript intervals.

Constraints:
- YouTube API limitations
- Retention resolution
- OAuth requirements

Success criteria:
A real video produces an aligned dataset with
measurable coverage and no unexplained transformation.

Verification:
Real API request + raw response inspection +
alignment test.