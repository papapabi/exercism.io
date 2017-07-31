class Bob
  RESPONSES = { yelling: "Whoa, chill out!",
                question: "Sure.",
                silence: "Fine. Be that way!",
                default: "Whatever." }

  def self.hey(remark)
    normalized_remark = normalize(remark)
    if remark.end_with?("?")
      RESPONSES[:question]
    elsif remark.strip.empty?
      RESPONSES[:silence]
    elsif remark.upcase == remark && remark.downcase != remark
      RESPONSES[:yelling]
    else
      RESPONSES[:default]
    end
  end

  private
  def self.normalize(remark)
  end
end

module BookKeeping
  VERSION = 1
end
