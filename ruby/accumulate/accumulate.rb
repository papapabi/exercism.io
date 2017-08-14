module Enumerable
  def accumulate()
    accumulator = []
    if block_given?
      each { |e| accumulator << yield(e) }
    else
      accumulator << to_enum(:accumulate)
    end
    accumulator
  end
end

module BookKeeping
  VERSION = 1
end

