<script>
	import Navbar from "$lib/components/layout/Navbar.svelte";
	import Footer from "$lib/components/layout/Footer.svelte";
	import Container from "$lib/components/layout/Container.svelte";
	import { ArrowLeft, Sparkles, ChevronDown } from "@lucide/svelte";
	import { slide } from "svelte/transition";

	const faqs = [
		{
			question: "Is ReadyHire free?",
			answer: "Yes. The Starter plan is completely free. You can scan resumes and generate full keyword alignment analyses without paying anything."
		},
		{
			question: "What file formats are supported?",
			answer: "We support PDF and DOCX files. For best results, ensure your document has highlightable text and is not an image scan."
		},
		{
			question: "How accurate is the AI analysis?",
			answer: "Highly accurate. We run advanced language models that match context-aware keywords and industry terminology."
		},
		{
			question: "Is my resume stored?",
			answer: "No. Your file is processed dynamically in-memory. We do not store your files permanently or share details with third parties."
		},
		{
			question: "Can I download my report?",
			answer: "Yes. You can download the completed report, including keyword reviews, cover letters, and interview questions, from the dashboard."
		}
	];

	let openIndex = $state(null);

	function toggle(index) {
		openIndex = openIndex === index ? null : index;
	}
</script>

<div class="min-h-screen bg-background text-foreground transition-colors duration-300 relative overflow-hidden">
	<!-- Ambient glow grids -->
	<div class="absolute inset-0 -z-10 bg-[linear-gradient(to_right,#8080800a_1px,transparent_1px),linear-gradient(to_bottom,#8080800a_1px,transparent_1px)] bg-[size:14px_24px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)]"></div>

	<!-- Navigation Bar -->
	<Navbar />

	<main class="py-16 md:py-24">
		<Container>
			<!-- Back Navigation -->
			<div class="mb-8">
				<a
					href="/"
					class="inline-flex items-center gap-2 rounded-lg border border-border bg-card px-4 py-2 text-sm font-semibold text-muted-foreground hover:text-foreground transition-all hover:border-[#408175]/30 shadow-sm"
				>
					<ArrowLeft class="h-4 w-4 text-[#408175]" />
					<span>Back to Homepage</span>
				</a>
			</div>

			<!-- Hero / Intro -->
			<div class="flex flex-col items-center text-center max-w-3xl mx-auto space-y-6 mb-16">
				<div class="inline-flex items-center gap-1.5 rounded-full border border-[#408175]/30 bg-[#2E4540]/25 px-3.5 py-1 text-xs font-semibold text-[#408175]">
					<Sparkles class="h-3.5 w-3.5" />
					<span>FAQ Hub</span>
				</div>

				<h1 class="text-4xl md:text-5xl font-extrabold tracking-tight leading-none">
					Frequently Asked <span class="bg-gradient-to-r from-[#2E4540] to-[#408175] bg-clip-text text-transparent">Questions</span>
				</h1>

				<p class="text-base md:text-lg text-muted-foreground max-w-xl leading-relaxed">
					Got questions about the ReadyHire analyzer? Find quick and simple answers right here.
				</p>
			</div>

			<!-- Accordion Section -->
			<div class="max-w-3xl mx-auto space-y-4">
				{#each faqs as faq, i}
					<div class="border border-border/60 bg-card/60 backdrop-blur-md rounded-2xl overflow-hidden transition-all duration-300">
						<button
							onclick={() => toggle(i)}
							class="w-full text-left p-6 font-bold text-base md:text-lg flex items-center justify-between gap-4 text-foreground hover:bg-[#2E4540]/5 transition-colors cursor-pointer select-none"
							aria-expanded={openIndex === i}
						>
							<span>{faq.question}</span>
							<ChevronDown
								class="h-5 w-5 text-muted-foreground transition-transform duration-300 shrink-0 {openIndex === i ? 'rotate-180 text-[#408175]' : ''}"
							/>
						</button>
						
						{#if openIndex === i}
							<div transition:slide={{ duration: 250 }}>
								<div class="px-6 pb-6 text-sm md:text-base text-muted-foreground leading-relaxed border-t border-border/10 pt-4">
									{faq.answer}
								</div>
							</div>
						{/if}
					</div>
				{/each}
			</div>
		</Container>
	</main>

	<!-- Footer -->
	<Footer />
</div>
