  spans ← CreateArray(n)
  for i ← 0 to n do
  k ← 1
  span_end ← false
  while i − k ≥ 0 and not span_end do
  if quotes[i − k] ≤ quotes[i] then
  k ← k + 1
  else
  span_end ← true
  spans[i] ← k
  return spans
