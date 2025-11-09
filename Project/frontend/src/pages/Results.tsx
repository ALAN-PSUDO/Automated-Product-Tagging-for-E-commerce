import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { ThumbsUp, Sparkles } from "lucide-react";
import Navigation from "@/components/Navigation";
import TagBubble from "@/components/TagBubble";
import { toast } from "sonner";

const Results = () => {
  const [image, setImage] = useState<string | null>(null);
  const [predictedTags, setPredictedTags] = useState<string[]>([]);
  const [predictedPrice, setPredictedPrice] = useState<string>("$0.00");
  const navigate = useNavigate();

  useEffect(() => {
    // Retrieve uploaded image
    const savedImage = localStorage.getItem("uploadedImage");
    const price = localStorage.getItem("predictedPrice");
    const cnnOutputStr = localStorage.getItem("cnnOutput");

    if (!savedImage || !price) {
      toast.error("No prediction data found. Please upload an image first.");
      navigate("/upload");
      return;
    }

    setImage(savedImage);
    setPredictedPrice(price.startsWith("₹") || price.startsWith("$") ? price : `₹${price}`);

    // Convert CNN raw output into pseudo-tags (or fetch from mlb_classes.json if available)
    if (cnnOutputStr) {
      try {
        const cnnData = JSON.parse(cnnOutputStr);
        const topIndices = getTopIndices(cnnData[0], 5); // Top 5 outputs
        loadTagLabels(topIndices);
      } catch (err) {
        console.error("Failed to parse CNN output:", err);
      }
    }
  }, [navigate]);

  // Helper to get top indices by value
  const getTopIndices = (arr: number[], n: number) => {
    return [...arr.keys()]
      .sort((a, b) => arr[b] - arr[a])
      .slice(0, n);
  };

  // Load tag labels (from public/mlb_classes.json if available)
  const loadTagLabels = async (indices: number[]) => {
    try {
      const res = await fetch("/mlb_classes.json");
      if (!res.ok) throw new Error("No tag labels file found");
      const labels: string[] = await res.json();
      const topTags = indices.map((i) => labels[i] || `Tag-${i + 1}`);
      setPredictedTags(topTags);
    } catch {
      // fallback if no file
      setPredictedTags(indices.map((i) => `Feature-${i + 1}`));
    }
  };

  const handleRateClick = () => {
    navigate("/feedback");
  };

  if (!image) return null;

  return (
    <div className="min-h-screen bg-background">
      <Navigation />
      
      <main className="container mx-auto px-4 pt-32 pb-20">
        <div className="max-w-4xl mx-auto space-y-8">
          <div className="text-center space-y-4 animate-fade-in">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-muted border border-border">
              <Sparkles className="w-4 h-4 text-primary" />
              <span className="text-sm font-medium text-muted-foreground">
                AI Analysis Complete
              </span>
            </div>
            <h1 className="text-4xl md:text-5xl font-bold">AI Predictions</h1>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {/* Left side — Uploaded image */}
            <Card className="p-6 shadow-soft animate-scale-in">
              <img
                src={image}
                alt="Uploaded clothing"
                className="w-full rounded-lg"
              />
            </Card>

            {/* Right side — AI Results */}
            <div className="space-y-6 animate-slide-up">
              <Card className="p-6 shadow-soft">
                <h2 className="text-2xl font-bold mb-4">Predicted Tags</h2>
                {predictedTags.length > 0 ? (
                  <div className="flex flex-wrap gap-3">
                    {predictedTags.map((tag, index) => (
                      <TagBubble key={tag} tag={tag} index={index} />
                    ))}
                  </div>
                ) : (
                  <p className="text-muted-foreground">
                    Tags are being generated...
                  </p>
                )}
              </Card>

              <Card className="p-6 shadow-soft bg-gradient-card">
                <h2 className="text-2xl font-bold mb-2">Predicted Price</h2>
                <div className="text-5xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                  {predictedPrice}
                </div>
              </Card>

              <Card className="p-6 shadow-soft bg-muted/30">
                <p className="text-sm text-muted-foreground leading-relaxed">
                  Predictions are generated using a hybrid CNN + XGBoost model trained on fashion data.
                </p>
              </Card>

              <Button
                onClick={handleRateClick}
                size="lg"
                className="w-full shadow-soft hover:shadow-hover transition-all duration-300"
              >
                <ThumbsUp className="w-5 h-5 mr-2" />
                Give Feedback
              </Button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Results;
