<script>
	import Navbar from "$lib/components/layout/Navbar.svelte";
	import Footer from "$lib/components/layout/Footer.svelte";
	import Container from "$lib/components/layout/Container.svelte";
	import { ArrowLeft, Sparkles, Upload, FileText, Cpu, CheckCircle } from "@lucide/svelte";
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
					<span>Simple 4-Step Process</span>
				</div>

				<h1 class="text-4xl md:text-5xl font-extrabold tracking-tight leading-none">
					How <span class="bg-gradient-to-r from-[#2E4540] to-[#408175] bg-clip-text text-transparent">ReadyHire Works</span>
				</h1>

				<p class="text-base md:text-lg text-muted-foreground max-w-xl leading-relaxed">
					Optimizing your applications is simple and instantaneous. Follow our straightforward workflow to unlock career growth.
				</p>
			</div>

			<!-- Step Cards Timeline -->
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto relative">
				<!-- Card 1 -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm relative flex flex-col justify-between overflow-hidden">
					<div class="absolute top-4 right-4 text-4xl font-black text-[#408175]/15 select-none group-hover:text-[#408175]/30 transition-colors">
						01
					</div>
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-6">
							<Upload class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">Upload Resume</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Provide your current resume in PDF or DOCX format for structure parsing.
						</p>
					</div>
				</div>

				<!-- Card 2 -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm relative flex flex-col justify-between overflow-hidden">
					<div class="absolute top-4 right-4 text-4xl font-black text-[#408175]/15 select-none group-hover:text-[#408175]/30 transition-colors">
						02
					</div>
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-6">
							<FileText class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">Paste Job Description</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Paste the target job description to match skills, responsibilities, and stack.
						</p>
					</div>
				</div>

				<!-- Card 3 -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm relative flex flex-col justify-between overflow-hidden">
					<div class="absolute top-4 right-4 text-4xl font-black text-[#408175]/15 select-none group-hover:text-[#408175]/30 transition-colors">
						03
					</div>
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-6">
							<Cpu class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">AI Analysis</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Our models cross-reference details to detect keyword gaps and compliance issues.
						</p>
					</div>
				</div>

				<!-- Card 4 -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm relative flex flex-col justify-between overflow-hidden">
					<div class="absolute top-4 right-4 text-4xl font-black text-[#408175]/15 select-none group-hover:text-[#408175]/30 transition-colors">
						04
					</div>
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-6">
							<CheckCircle class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">Receive Personalized Report</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Get your readiness score, rewrite suggestions, cover letter draft, and prep questions.
						</p>
					</div>
				</div>
			</div>
		</Container>
	</main>

	<!-- Footer -->
	<Footer />
</div>
