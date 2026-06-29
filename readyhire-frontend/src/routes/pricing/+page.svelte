<script>
	import Navbar from "$lib/components/layout/Navbar.svelte";
	import Footer from "$lib/components/layout/Footer.svelte";
	import Container from "$lib/components/layout/Container.svelte";
	import { ArrowLeft, Sparkles, Check } from "@lucide/svelte";
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
					<span>Flexible Plans</span>
				</div>

				<h1 class="text-4xl md:text-5xl font-extrabold tracking-tight leading-none">
					Simple, Transparent <span class="bg-gradient-to-r from-[#2E4540] to-[#408175] bg-clip-text text-transparent">Pricing</span>
				</h1>

				<p class="text-base md:text-lg text-muted-foreground max-w-xl leading-relaxed">
					Find the right fit for your career stage. Get started for free, with advanced options launching soon.
				</p>
			</div>

			<!-- Pricing Grid -->
			<div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto items-stretch">
				<!-- Starter Plan (Highlighted) -->
				<div class="p-8 rounded-3xl border-2 border-[#408175] bg-card/80 backdrop-blur-md shadow-lg relative flex flex-col justify-between overflow-hidden transform md:-translate-y-2 transition-all">
					<div class="absolute top-0 right-0 bg-[#408175] text-white text-xs font-bold px-4 py-1.5 rounded-bl-xl uppercase tracking-wider">
						Available Now
					</div>
					
					<div class="space-y-6">
						<div>
							<h3 class="font-bold text-xl text-foreground">Starter</h3>
							<p class="text-xs text-muted-foreground mt-1">Perfect for immediate resume optimization</p>
						</div>

						<div class="flex items-baseline gap-1">
							<span class="text-4xl font-extrabold text-foreground">Free</span>
							<span class="text-xs text-muted-foreground">/ forever</span>
						</div>

						<hr class="border-border/60" />

						<ul class="space-y-3.5 text-sm">
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-[#408175] shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Full AI Resume Analysis</span>
							</li>
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-[#408175] shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">ATS Keyword Matching</span>
							</li>
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-[#408175] shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Tailored Cover Letter Draft</span>
							</li>
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-[#408175] shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Interview Practice Questions</span>
							</li>
						</ul>
					</div>

					<div class="pt-8 mt-auto">
						<a
							href="/#analyzer"
							class="flex h-11 items-center justify-center rounded-xl bg-[#2E4540] hover:bg-[#408175] text-white font-semibold shadow-sm transition-all active:scale-[0.98] w-full text-center text-sm"
						>
							Start Free Scan
						</a>
					</div>
				</div>

				<!-- Professional Plan (Coming Soon) -->
				<div class="p-8 rounded-3xl border border-border/60 bg-card/40 backdrop-blur-sm shadow-sm relative flex flex-col justify-between transition-all opacity-85 hover:opacity-100">
					<div class="space-y-6">
						<div>
							<h3 class="font-bold text-xl text-foreground">Professional</h3>
							<p class="text-xs text-muted-foreground mt-1">Accelerated analytics and smart variations</p>
						</div>

						<div class="flex items-baseline gap-1">
							<span class="text-3xl font-bold text-foreground">Coming Soon</span>
						</div>

						<hr class="border-border/60" />

						<ul class="space-y-3.5 text-sm">
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-muted-foreground/50 shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Everything in Starter</span>
							</li>
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-muted-foreground/50 shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Unlimited scans per month</span>
							</li>
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-muted-foreground/50 shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Advanced AI resume restructuring</span>
							</li>
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-muted-foreground/50 shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Interactive interview coaching mockups</span>
							</li>
						</ul>
					</div>

					<div class="pt-8 mt-auto">
						<button
							disabled
							class="flex h-11 items-center justify-center rounded-xl border border-border bg-muted/50 text-muted-foreground font-semibold w-full text-center text-sm cursor-not-allowed"
						>
							Coming Soon
						</button>
					</div>
				</div>

				<!-- Enterprise Plan (Coming Soon) -->
				<div class="p-8 rounded-3xl border border-border/60 bg-card/40 backdrop-blur-sm shadow-sm relative flex flex-col justify-between transition-all opacity-85 hover:opacity-100">
					<div class="space-y-6">
						<div>
							<h3 class="font-bold text-xl text-foreground">Enterprise</h3>
							<p class="text-xs text-muted-foreground mt-1">For organizations and career advisors</p>
						</div>

						<div class="flex items-baseline gap-1">
							<span class="text-3xl font-bold text-foreground">Coming Soon</span>
						</div>

						<hr class="border-border/60" />

						<ul class="space-y-3.5 text-sm">
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-muted-foreground/50 shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Everything in Professional</span>
							</li>
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-muted-foreground/50 shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Team workflow dashboards</span>
							</li>
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-muted-foreground/50 shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">Dedicated career coach advisory</span>
							</li>
							<li class="flex items-start gap-2.5">
								<Check class="h-4.5 w-4.5 text-muted-foreground/50 shrink-0 mt-0.5" />
								<span class="text-muted-foreground leading-snug">API access for system integrations</span>
							</li>
						</ul>
					</div>

					<div class="pt-8 mt-auto">
						<button
							disabled
							class="flex h-11 items-center justify-center rounded-xl border border-border bg-muted/50 text-muted-foreground font-semibold w-full text-center text-sm cursor-not-allowed"
						>
							Coming Soon
						</button>
					</div>
				</div>
			</div>
		</Container>
	</main>

	<!-- Footer -->
	<Footer />
</div>
