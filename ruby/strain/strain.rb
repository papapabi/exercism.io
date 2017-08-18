module Enumerable
  def keep(&block)
    if block_given?
      [].tap { |result| each { |e| yield(e) ? result << e : nil } }
    end
  end

  def discard(&block)
    if block_given?
      [].tap { |result| each { |e| yield(e) ? nil : result << e } }
    end
  end
end
