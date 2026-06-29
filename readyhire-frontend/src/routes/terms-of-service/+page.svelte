<script>
	import Navbar from "$lib/components/layout/Navbar.svelte";
	import Footer from "$lib/components/layout/Footer.svelte";
	import Container from "$lib/components/layout/Container.svelte";
	import { ArrowLeft, FileText, Award, AlertTriangle, Cloud, ShieldAlert } from "@lucide/svelte";
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
					<FileText class="h-3.5 w-3.5" />
					<span>User Agreement</span>
				</div>

				<h1 class="text-4xl md:text-5xl font-extrabold tracking-tight leading-none">
					Terms of <span class="bg-gradient-to-r from-[#2E4540] to-[#408175] bg-clip-text text-transparent">Service</span>
				</h1>

				<p class="text-base md:text-lg text-muted-foreground max-w-xl leading-relaxed">
					Please read our terms of service before using our resume optimization tools.
				</p>
			</div>

			<!-- Terms Sections Grid -->
			<div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8 max-w-4xl mx-auto">
				<!-- Educational & Career Purpose -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<Award class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">Educational & Career Purpose</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						ReadyHire is an educational coaching utility designed to analyze job fit parameters and help structure applications. It does not replace certified professional advice.
					</p>
				</div>

				<!-- AI-Generated Recommendations -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<FileText class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">AI-Generated Recommendations</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						All compatibility reports, rewrite recommendations, drafts, and preparation queries are generated dynamically by AI and do not guarantee hiring outcomes.
					</p>
				</div>

				<!-- User Responsibility -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<AlertTriangle class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">User Responsibility</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						You maintain full responsibility for the files you upload. Ensure you possess legal rights to share the text contents and that details are truthful and authentic.
					</p>
				</div>

				<!-- Service Availability -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<Cloud class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">Service Availability</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						We provide our service as-is and as-available. We aim to keep ReadyHire online but make no guarantees about uptime, server delays, or continuous feature availability.
					</p>
				</div>

				<!-- Limitation of Liability -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3 md:col-span-2">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<ShieldAlert class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">Limitation of Liability</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						ReadyHire and its founders are not responsible or liable for any career rejection, job application status, loss of employment opportunity, or decisions made based on reports.
					</p>
				</div>
			</div>
		</Container>
	</main>

	<!-- Footer -->
	<Footer />
</div>
