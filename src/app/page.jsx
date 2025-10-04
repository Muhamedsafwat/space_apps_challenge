import Hero from "./_components/Hero";
import Navbar from "./_components/Navbar";
import Challenges from "./_components/Challenges";
import Gallery from "./_components/Gallery";
import Nisar from "./_components/Nisar";
import Sample from "./_components/Sample";
import Footer from "./_components/Footer";
import Chatbot from "./_components/Chatbot";
import LiveData from "./_components/LiveData";
import AiChat from "./_components/AiChat";

export default function Home() {
  return (
    <>
      <div className="relative flex flex-col min-h-screen w-full bg-background">
        <Navbar />
        <Hero />
        <div className="layout-container flex h-full grow flex-col">
          <main className="flex flex-1 justify-center py-12 px-4 sm:px-6 lg:px-8">
            <div className="layout-content-container flex flex-col max-w-4xl flex-1 gap-16">
              <Challenges />
              <Gallery />
              <Nisar />
              <Sample />
              <LiveData />
              <AiChat />
            </div>
          </main>
        </div>
        <Footer />
      </div>
    </>
  );
}
